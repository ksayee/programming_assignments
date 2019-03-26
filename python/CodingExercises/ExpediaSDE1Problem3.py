'''
Find the length of the longest subarray whose values all share a single common factor.
For this subarray, the factor may be chosen from a list of input values; called factor array.

Example
Given  Result
Search Array:
[3,3,1,4,30,12,9,6,1,9,9,9,9,3,3,3]
Factor Array: [ 3,4]   Return :7
[3,3,1,4,30,12,9,6,1,9,9,9,9,3,3,3]
Common Factor: 3
Search Array:
[2, 4, 6, 10, 30, 25, 15, 5, 10, 18]
Factor Array :[ 2, 5]  Return: 6
[2, 4, 6, 10, 30, 25, 15, 5, 10, 18]

Common Factor: 5
'''

def ExpediaSDE1Problem3(ary,lst):

    dict={}

    for key in lst:
        flg=False

        for i in range(0,len(ary)):
            if ary[i]%key==0:
                if flg==False:
                    idx=i
                    flg=True
            else:
                if flg==True:
                    if key in dict.keys():
                        dict[key].append(ary[idx:i])
                    else:
                        tmp=[]
                        tmp.append(ary[idx:i])
                        dict[key]=tmp
                flg=False
        if flg==True:
            if key in dict.keys():
                dict[key].append(ary[idx:i+1])
            else:
                tmp=[]
                tmp.append(ary[idx:i+1])
                dict[key]=tmp

    tmp=[]
    for key,val in dict.items():
        for lst in val:
            if len(tmp)==0:
                tmp=lst.copy()
            else:
                if len(lst)>len(tmp):
                    tmp=lst.copy()
    return tmp

def main():

    ary=[3,3,1,4,30,12,9,6,1,9,9,9,9,3,3,3]
    lst=[3,4]
    print(ExpediaSDE1Problem3(ary,lst))

    ary = [2, 4, 6, 10, 30, 25, 15, 5, 10, 18]
    lst = [2,5]
    print(ExpediaSDE1Problem3(ary, lst))

if __name__=='__main__':
    main()