'''
Iterative HeapSort
HeapSort is a comparison based sorting technique where we first build Max Heap and then swaps the root element with last element (size times) and maintains the heap property each time to finally make it sorted.

Examples:

Input :  10 20 15 17 9 21
Output : 9 10 15 17 20 21

Input:  12 11 13 5 6 7 15 5 19
Output: 5 5 6 7 11 12 13 15 19
'''

def CreateHeap(ary):

    lst=[]
    for i in range(0,len(ary)):
        lst.append(ary[i])
        k=i
        while k>0:
            if k%2==0:
                p=(k//2)-1
            else:
                p=k//2
            if lst[k]>lst[p]:
                tmp=lst[p]
                lst[p]=lst[k]
                lst[k]=tmp
            k=k-1
    return lst

def HeapSort(ary):

    lst=CreateHeap(ary)
    print(lst)
    fnl_lst=[]
    while len(lst)!=0:
        fnl_lst.append(lst[0])
        lst[0]=lst[-1]
        lst.pop()
        i=0
        j=(2*i)+1
        while j<len(lst)-1:
            if lst[j+1]>lst[j]:
                j=j+1
            if lst[i]<lst[j]:
                tmp=lst[i]
                lst[i]=lst[j]
                lst[j]=tmp
                i=j
                j=2*j+1
    return fnl_lst

def main():

    ary=[10,20,15,17,9,21]
    print(HeapSort(ary))

    ary = [12,11,13,5,6,7,15,5,19]
    print(HeapSort(ary))

if __name__=='__main__':
    main()