from sys import argv

script, filename = argv

print(f"We're going to eraase {filename}.")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = opem(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now, I'm going to ask you for three lines.")