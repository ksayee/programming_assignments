# Check Whether a number is Duck Number or not
# A Duck number is a number which has zeroes present in it, but there should be no zero present in the beginning of the number. For example 3210, 8050896, 70709 are all duck numbers whereas 02364, 03401 are not.
# The task is to check whether the given number is a duck number or not.

def DuckNumber(n):

    lst=list(n)

    if lst[0]=='0' or lst[-1]=='0':
        return False
    else:
        for i in range(1,len(lst)-1):
            key=lst[i]
            if key=='0':
                return True

def main():

    n='707069'
    print(DuckNumber(n))

    n ='02364'
    print(DuckNumber(n))

if __name__=='__main__':
    main()