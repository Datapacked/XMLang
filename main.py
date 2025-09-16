import xml.etree.ElementTree as ET
import sys

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
	argstr = argstr[:-2]
	print(argstr)
	return



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