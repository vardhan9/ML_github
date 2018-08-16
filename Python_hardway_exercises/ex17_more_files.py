from sys import argv
from os.path import exists

script,from_file,to_file=argv

print("copying from %s to %s"%(from_file,to_file))

in_file=open(from_file)
indata = in_file.read()

print("input data is %d bytes")%len(indata)

print("does output file exixts ? %r")%exists(to_file)
print ("Ready,hit ENTER to continue, CTRCl-C to abort")
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print ("Alright, Done")

out_file.close()
in_file.close()
