from amath import is_even

def main():
	tlist = [10,21,27,35,0,-42,-23,666,123,000]
	for a in tlist:
		if(is_even(a) == True):
			print("a is even",a)
		else:
			print("a is odd",a)
		
if (__name__=="__main__"):
	main()