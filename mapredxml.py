#!/usr/bin/python36

import xml.etree.ElementTree as ET

print("Enter JobTracker Hostname: ", end=' ')
host = input()

mapredfile = ET.parse('/etc/hadoop/mapred-site.xml')
root = mapredfile.getroot()
a = ET.SubElement(root, "property")
b = ET.SubElement(a, "name")
b.text = "mapred.job.tracker"
c = ET.SubElement(a, "value")
c.text = "{}:9002".format(host)
tree = ET.ElementTree(root)
tree.write('/etc/hadoop/mapred-site.xml')