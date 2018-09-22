'''
443. String Compression
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
'''

def LeetCode443(ary):

    lst=[]

    prev_chr=ary[0]
    cnt=1
    for i in range(1,len(ary)):
        curr_chr=ary[i]

        if prev_chr!=curr_chr:
            lst.append(prev_chr)
            lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev_chr=curr_chr

    lst.append(prev_chr)
    lst.append(str(cnt))

    return lst

def main():

    ary=["a","a","b","b","c","c","c"]
    print(LeetCode443(ary))

    ary = ["a"]
    print(LeetCode443(ary))

if __name__=='__main__':
    main()