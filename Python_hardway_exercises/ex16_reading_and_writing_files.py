
from sys import argv
script, filename =argv

print ("we are going to erase %r" %filename)
print ("if you dont want that hit CTRL-C")
print ("press ENTER to continue")

raw_input("?")

print ("openeing the file......")

target=open(filename,'w')

print ("erasing the file . bye")

target.truncate()

print ("Now, i am ging to ask three new lines")

line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print ("i am going to write these lines to the file")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")


target.write(line3)
target.write("\n")

target.close()

print("D O N E")
