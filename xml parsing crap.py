import xml.etree.ElementTree as etree
import random
#for child in Gang:
   #print child.tag, child.attrib
#print Gang[6][0][0].text

#MadeUpName = etree.parse ("filename.xml")
#x = MadeUpName.getroot ()

#importatnt things here are the import line, etree.parse and getroot

xmlDoc = etree.parse('test2.xml')
Gang = xmlDoc.getroot()
#print Gang.tag
#print Gang
#print Gang.attrib

#root = tree.getroot()

for territories in Gang.iter('territory_name'):
    print territories.text
##inputName = raw_input('which ganger: ')
##
##for gangers in Gang.findall('gangers'):
##    for ganger in gangers.findall('ganger'):
##        name = ganger.find('name').text
##        if name == inputName:
##            print name
##            BS = ganger.find('bs').text
##            print BS
##DieRoll = random.randint(1,6)
##print DieRoll
##if DieRoll + int(BS) >7:
##    print 'HIT!'
##else:
##    print 'Miss'
