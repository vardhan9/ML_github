x="there are %d types of people"%10
binary="binary"
do_not="dont"
y="those who know %s and those who %s"%(binary,do_not)

print x
print y
print "i said :%r"%x
print"i also said : '%s'."%y


hilarious= False
joke_evaluation="is that funny ? %r"

print joke_evaluation%hilarious

w="this is teh left side of "
e="a string with right side"

print w+e