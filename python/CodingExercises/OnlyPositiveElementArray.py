# Only integer with positive value in positive negative value in array
# Given an array of N integers. In the given, for each positive element ‘x’ there exist a negative value ‘-x’,
# except one integer whose negative value is not present. That integer may occur multiple number of time. The task is find that integer.

def OnlyPositiveElementArray(ary):

    dict={}

    for l in ary:
        if abs(l) in dict.keys():
            tmp=dict[abs(l)].copy()
            tmp.append(l)
            dict[abs(l)]=list(set(tmp))
        else:
            tmp=[]
            tmp.append(l)
            dict[abs(l)]=tmp

    for key,val in dict.items():
        if len(val)==1:
            return key

    return "None"

def main():

    ary=[ 1, 8, -6, -1, 6, 8, 8 ]
    print(OnlyPositiveElementArray(ary))

    ary = [15, 6, -9, 4, 15, 9,-6, -4, 15, 15]
    print(OnlyPositiveElementArray(ary))

if __name__=='__main__':
    main()