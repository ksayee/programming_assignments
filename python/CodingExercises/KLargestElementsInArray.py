'''
k largest(or smallest) elements in an array | added Min Heap method
Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3
then your program should print 50, 30 and 23.
'''

def CreateMaxHeap(ary):
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
                tmp=lst[k]
                lst[k]=lst[p]
                lst[p]=tmp
            k=k-1
    return lst
def KLargestElementsInArray(ary):

    lst=CreateMaxHeap(ary)
    print(lst)
    sort_lst=[]
    counter=0
    while counter<3:
        sort_lst.append(lst[0])
        lst[0]=lst[-1]
        lst.pop()
        i=0
        j=(2*i)+1
        while j<len(lst)-1:
            if lst[j+1]>lst[j]:
                j=j+1
            if lst[j]>lst[i]:
                tmp=lst[i]
                lst[i]=lst[j]
                lst[j]=tmp
            i=j
            j=(2*j)+1
        counter=counter+1
    return sort_lst
def main():

    ary=[1, 23, 12, 9, 30, 2, 50]
    print(KLargestElementsInArray(ary))

if __name__=='__main__':
    main()