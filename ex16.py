#Tells the program a user will enter a var for script
from sys import argv

#tells us that the var will be the "filename"
script, filename = argv

#f string allows the Var t o be printed, in this case "filename"
#htese prints are just text that options for possible commmands
print(f"We're going to erase {filename}.")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

#print to prompt user to use CTRL-C or RETURN
input("?")

#Target opens the filename from argv, print is just text
print("Opening the file...")
target = open(filename, 'w')

#truncate erases the contents of file!
print("Truncating the file. Goodbye!")
target.truncate()

#This print states whats coming up
print("Now, I'm going to ask you for three lines.")

# 3 vars requiring input, the "" allows for a prompt to print with input request
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

#print saying whats next
print("I'm going to write these to the file")

#target.write says to write to sepcifid file "filename"
#() takes the var and uses this as input for filename
#\n starts a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#acts as a save, essenitally completes the program
print("And finally, we close it.")
target.close()