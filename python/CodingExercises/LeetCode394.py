'''
394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

def LeetCode394(str1):

    fnl_lst=[]
    lst=[]
    for i in range(0,len(str1)):

        key=str1[i]

        if key==']':
            tmp=[]
            while lst[-1]!='[':
                tmp.append(lst[-1])
                lst.pop()

            tmp.reverse()
            lst.pop()
            num=int(lst[-1])
            lst.pop()
            i=0
            if len(lst)==0:
                while i < num:
                    fnl_lst.append(''.join(tmp))
                    i = i + 1
            else:
                while i<num:
                    lst.append(''.join(tmp))
                    i=i+1
        else:
            lst.append(key)
    if len(lst)>0:
        fnl_lst.append(''.join(lst))

    return ''.join(fnl_lst)

def main():
    
    str1='3[a]2[bc]'
    print(LeetCode394(str1))

    str1 = '3[a2[c]]'
    print(LeetCode394(str1))

    str1 = '2[abc]3[cd]ef'
    print(LeetCode394(str1))

    str1 = '2[ab2[cd3[hi]2[zz]]]www'
    print(LeetCode394(str1))

if __name__=='__main__':
    main()