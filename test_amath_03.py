from amath import is_even

def main():
	for a in range(10):
		if(is_even(a) == True):
			print("a is even",a)
		else:
			print("a is odd",a)
		
if (__name__=="__main__"):
	main()