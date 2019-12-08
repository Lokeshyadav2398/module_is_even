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
            print(f"For {a[0]} is_even retval :{rvalue} expected :{a[1]}, FAIL")
        """
        else:
            print(f"For {a[0]} is_even retval :{rvalue} expected :{a[1]}, PASS")
        """
if (__name__=="__main__"):
    main()
