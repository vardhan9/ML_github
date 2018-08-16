def argument(*args):
	arg1,arg2=args
	print "this arg1 : %r and arg2:%r"%(arg1,arg2)

def one_argument(arg1):
	print"this is one_argument : %r"%arg1
	
def no_arguments():
	print"noting"

argument("Raja","Vardhan")
one_argument("Marthala")
no_arguments()