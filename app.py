import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
root = tree.getroot()
for country in root.findall('country'):
     name = country.get('name')
     rank = country.find('rank').text
     print (name , rank)