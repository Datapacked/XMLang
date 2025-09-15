import xml.etree.ElementTree as ET
import sys

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
	print(f"Tag: {child.tag}, Text: {child.text}, name {child.attrib['name']}")