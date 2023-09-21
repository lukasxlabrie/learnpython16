#tells terminal that argv will be a var via input prior to running script
from sys import argv

#tells us that argv will need the script name and that argv will be used later as filename
script, filename = argv

#opens the file
txt = open (filename)

#prints the contents of filename
print (f"Here's your file {filename}:")
print(txt.read)()
