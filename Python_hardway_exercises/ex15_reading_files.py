from sys import argv
scrip,filename = argv
txt = open(filename)
print("Here is your file name %r"%filename)
print txt.read()


print ("Type filename here : ")
filename_again = raw_input("-->")

txt_again = open(filename_again)
print txt_again.read()
