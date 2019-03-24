'''
Only integer with positive value in positive negative value in array
Given an array of N integers. In the given,
for each positive element ‘x’ there exist a negative value ‘-x’,
except one integer whose negative value is not present.
That integer may occur multiple number of time. The task is find that integer.

Examples:

Input : arr[] = { 1, 8, -6, -1, 6, 8, 8 }
Output : 8
All positive elements have an equal negative
value except 8.

Input : arr[] = { 15, 6, -9, 4, 15, 9,
                      -6, -4, 15, 15 }
Output : 15
'''

def OnlyPositiveIntegerArray(ary):

    fnl_lst=[]
    dict={}

    for key in ary:

        if key<0:
            if (-1)*key in dict.keys():
                del dict[(-1)*key]
            else:
                dict[(-1) * key]=-1
        else:
            if key not in dict.keys():
                dict[key]=1

    for key,val in dict.items():
        if val==1:
            fnl_lst.append(key)

    return fnl_lst

def main():

    ary=[1, 8, -6, -1, 6, 8, 8]
    print(OnlyPositiveIntegerArray(ary))

    ary = [15, 6, -9, 4, 15, 9,-6, -4, 15, 15]
    print(OnlyPositiveIntegerArray(ary))

if __name__=='__main__':
    main()