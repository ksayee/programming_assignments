'''
Given two binary max heaps as arrays, merge the given heaps.
Examples :
Input  : a = {10, 5, 6, 2},
         b = {12, 7, 9}
Output : {12, 10, 9, 2, 5, 7, 6}
'''

def CreateMaxHeap(ary1,ary2):

    lst=ary1.copy()
    while len(ary2)!=0:
        lst.append(ary2[0])
        ary2[0]=ary2[-1]
        ary2.pop()
        i=0
        j=(2*i)+1
        while j<len(ary2)-1:
            if ary2[j+1]>ary2[j]:
                j=j+1
            if ary2[j]>ary2[i]:
                tmp=ary2[i]
                ary2[i]=ary2[j]
                ary2[j]=tmp
            j=i
            j=(2*j)+1
        k = len(lst) - 1
        while k > 0:
            if k % 2 == 0:
                p = (k // 2) - 1
            else:
                p = k // 2
            if lst[k] > lst[p]:
                tmp = lst[p]
                lst[p] = lst[k]
                lst[k] = tmp
            k = k - 1
    return lst

def MergeTwoBinaryMaxHeap(ary1,ary2):
    lst=CreateMaxHeap(ary1,ary2)
    return lst

def main():

    ary1=[10, 5, 6, 2]
    ary2=[12, 7, 9]
    print(MergeTwoBinaryMaxHeap(ary1,ary2))

if __name__=='__main__':
    main()