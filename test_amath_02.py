from amath import is_even

def main():
	a = int(input("enter any number:"))
	if(is_even(a) == True):
		print("a is even")
	else:
		print("a is odd")
		
if (__name__=="__main__"):
	main()