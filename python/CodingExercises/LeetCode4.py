'''
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''


def LeetCode4(lst1,lst2):

    fnl_lst=lst1
    fnl_lst.extend(lst2)

    fnl_lst.sort()

    if len(fnl_lst)%2!=0:
        mid=int(len(fnl_lst)/2)
        return fnl_lst[mid]
    else:
        idx1=int(len(fnl_lst)/2)-1
        idx2=int(len(fnl_lst)/2)

        val=(fnl_lst[idx1]+fnl_lst[idx2])/2
        return val

def main():
    
    lst1=[1,3]
    lst2=[2]
    print(LeetCode4(lst1,lst2))

    lst1 = [1, 2]
    lst2 = [3, 4]
    print(LeetCode4(lst1, lst2))

if __name__=='__main__':
    main()