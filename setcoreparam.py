#!/usr/bin/python36

import xml.etree.ElementTree as ET

print("Enter Master Hostname: ", end=' ')
host = input()

corefile = ET.parse('/etc/hadoop/core-site.xml')
root = corefile.getroot()
a = ET.SubElement(root, "property")
b = ET.SubElement(a, "name")
b.text = "fs.default.name"
c = ET.SubElement(a, "value")
c.text = "hdfs://{}:9001".format(host)
tree = ET.ElementTree(root)
tree.write('/etc/hadoop/core-site.xml')