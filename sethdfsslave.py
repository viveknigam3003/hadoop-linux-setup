#!/usr/bin/python36

import xml.etree.ElementTree as ET

hdfsfile = ET.parse('/etc/hadoop/hdfs-site.xml')
root = hdfsfile.getroot()
a = ET.SubElement(root, "property")
b = ET.SubElement(a, "name")
b.text = "dfs.data.dir"
c = ET.SubElement(a, "value")
c.text = "/data"
tree = ET.ElementTree(root)
tree.write('/etc/hadoop/hdfs-site.xml')