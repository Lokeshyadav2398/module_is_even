from amath import is_even

def main():
	data = [
			[10,True],
			[21,False],
			[27,False],
			[35,False],
			[0,False],
			[-42,False],
			[23,False],
			[666,True],
			[123,False],
			[000,False]
			] 
	for a in data:
		rvalue = is_even(a[0])
		if(rvalue != a[1]):
			print(a[0],"fail")
		else:
			print(a[0],"pass")
if (__name__=="__main__"):
	main()