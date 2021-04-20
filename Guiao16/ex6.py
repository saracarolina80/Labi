from lxml import etree

def main():
	xml = etree.parse('conf.xml')
	root = xml.getroot()
	print(root.tag)
	for child in root:
		for child in child:
			print(child.tag, child.attrib, child.text)


main()
