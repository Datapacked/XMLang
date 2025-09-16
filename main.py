import xml.etree.ElementTree as ET
import sys

class MockFile:
	def __init__(self):
		self.content = ""
	def write(self, content):
		self.content = self.content + content

def arg_to_str(arg):
	if (arg.tag == 'arg'):
		return f"{arg.attrib['type']} {arg.attrib['name']}"
	if (arg.tag == 'aarg'):
		return f"{arg.attrib['type']}[] {arg.attrib['name']}"


# Converts function tag into a string

def handle_func(func, file):
	file.write(f"{func.attrib['type']} ")
	file.write(f"{func.attrib['name']}(")
	argstr = ""
	if func[0].tag != 'args':
		raise Exception("<args> must be the first tag inside <func>")
	for arg in func[0]:
		argstr = argstr + f"{arg_to_str(arg)}, "
	file.write(argstr[:-2])
	file.write(")\n")
	file.write("{\n")
	for tag in func[1::]:
		handle_tag(tag, file)
	file.write("}\n")
	return

# Handles assignment

def handle_assign(assign, file):
	file.write(f"{assign.attrib['name']} = ")
	for tag in assign:
		handle_tag(tag, file)
	file.write(";\n")

# Handles operator

def handle_operator(operator, file):
	file.write("(")
	F = MockFile()
	for tag in operator:
		handle_tag(tag, F)
		F.write(f" {operator.attrib['op']} ")
	F.content = F.content[:-(len(operator.attrib['op']) + 2)]
	file.write(F.content)
	file.write(")")

# Handles value

def handle_value(value, file):
	if value.attrib['type'] == "string": # If value is a string
		file.write(f'"{value.text}"')
	# If value is an uint8, uint16, uint32, uint64, int8, int16, int32, int64, float or double
	if (value.attrib['type'] in ['float', 'double']) or (value.attrib['type'] in ''.join([''.join([i, "u" + i]) for i in [f"int{n * 8}_t" for n in range(9)]])):
		file.write(f"(({value.attrib['type']}) {value.text})")

# Handles while

def handle_while(whiel, file):
	file.write("while ")
	if whiel[0].tag != 'condition':
		raise Exception("First tag inside <while> MUST be <condition>")
	file.write("(")
	for con in whiel[0]:
		handle_tag(con, file)
	file.write(")")
	file.write("{\n")
	for tag in whiel[1::]:
		handle_tag(tag, file)
	file.write("}\n")

# Handles if

def handle_if(fi, file):
	file.write("if ")
	if fi[0].tag != 'condition':
		raise Exception("First tag inside <while> MUST be <condition>")
	file.write("(")
	for con in fi[0]:
		handle_tag(con, file)
	file.write(")")
	file.write("{\n")
	for tag in fi[1::]:
		handle_tag(tag, file)
	file.write("}\n")

# Handles prop

def handle_prop(prop, file):
	file.write("(")
	for tag in prop:
		handle_tag(tag, file)
	file.write(f").{prop.attrib['prop']}")

# Handles cast

def handle_cast(cast, file):
	file.write(f"(({cast.attrib['type']}) (")
	for tag in cast:
		handle_tag(tag, file)
	file.write("))")

# Handles call

def handle_call(call, file):
	file.write(f"{call.attrib['name']}(")
	F = MockFile()
	for tag in call:
		handle_tag(tag, F)
		F.write(', ')
	F.content = F.content[:-2]
	file.write(F.content)
	file.write(")")

def handle_tag(tag, file):
	match(tag.tag):
		case 'func':
			handle_func(tag, file)
		case 'declare':
			file.write(f"{tag.attrib['type']} {tag.attrib['name']};\n")
		case 'adecl':
			file.write(f"{tag.attrib['type']}* {tag.attrib['name']} = ({tag.attrib['type']}*) malloc(sizeof({tag.attrib['type']}) * {int(tag.attrib['size'])});\n")
		case 'assign':
			handle_assign(tag, file)
		case 'operator':
			handle_operator(tag, file)
		case 'increment':
			file.write(f"{tag.attrib['name']}++;\n")
		case 'decrement':
			file.write(f"{tag.attrib['name']}--;\n")
		case 'value':
			handle_value(tag, file)
		case 'variable':
			file.write(tag.attrib['name'])
		case 'while':
			handle_while(tag, file)
		case 'if':
			handle_if(tag, file)
		case 'prop':
			handle_prop(tag, file)
		case 'cast':
			handle_cast(tag, file)
		case 'call':
			handle_call(tag, file)

BUILD_DIR = "./build/"

try:
	file = sys.argv[1]
except:
	file = "example.xml"

# Parse the XML file
tree = ET.parse(file)

# Get the root element of the XML tree
root = tree.getroot()

# Now you can traverse the tree and access elements and their attributes
# For example, to print the tag and text of each child of the root:
for child in root:
	print(f"Tag: {child.tag}, Text: {child.text}, name {child.attrib.get('name')}")
	if child.tag == 'main':
		f = open('build/main.cpp', 'w')
		f.write("#include <iostream>\n")
		f.write("#include <cstdint>\n")
		f.write('\n')
		for ch in child:
			if ch.tag == 'func':
				handle_func(ch, f)
		f.close()