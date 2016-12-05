import xml.etree.ElementTree as etree

totalInput = []

maxLength = raw_input("")


for i in range(0,int(maxLength)):
    xmlInput = raw_input("")
    totalInput.append(xmlInput)

finalInput = "".join(totalInput)

tree = etree.ElementTree(etree.fromstring(finalInput))

root = tree.getroot()

final = []
def count(node):
    totalAttrib = 0
    if len(node) == 0:
        if node.attrib != {}:
            totalAttrib += len(node.attrib)
    else:
        if node.attrib != {}:
            totalAttrib += len(node.attrib)

        for child in node:
            if len(child) > 0:
                count(child)
            else:
                if child.attrib != {}:
                    totalAttrib += len(child.attrib)
    final.append(totalAttrib)


count(root)

print sum(final)



