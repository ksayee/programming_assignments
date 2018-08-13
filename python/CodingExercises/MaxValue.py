# Calculate maximum value using ‘+’ or ‘*’ sign between two numbers in a string
# Given a string of numbers, the task is to find the maximum value from the string, you can add a ‘+’ or ‘*’ sign between any two numbers.

def MaxValue(str):

    lst=list(str)
    max_val=1
    tmp=[]

    for l in lst:
        if len(tmp)==0:
            tmp.append(int(l))
        else:
            if (tmp[-1]==1 or tmp[-1]==0) or (int(l)==0 or int(l)==1):
                tmp.append(tmp[-1]+int(l))
            else:
                tmp.append(tmp[-1]*int(l))
    return tmp[-1]

def main():
    
    str='01231'
    print(MaxValue(str))

    str = '891'
    print(MaxValue(str))

    str = '0158100'
    print(MaxValue(str))

if __name__=='__main__':
    main()