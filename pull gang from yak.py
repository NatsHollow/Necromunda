# creates and saves an xml file from the Yaktribe website using the gang ID you input.
#Error handling is not done yet
import urllib
gang = raw_input ('Enter your gang ID: ')
testfile = urllib.URLopener ()
testfile.retrieve ("https://yaktribe.org/necromunda/gang/xml/" + gang, gang + ".xml")


