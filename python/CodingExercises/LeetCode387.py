'''
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

def LeetCode387(str1):

    lst=list(str1)

    idx=-1
    for i in range(0,len(lst)):

        key=lst[i]
        if key not in lst[i+1:]:
            idx=i
            break


    return idx

def main():
    
    str1='leetcode'
    print(LeetCode387(str1))

    str1 = 'loveleetcode'
    print(LeetCode387(str1))

if __name__=='__main__':
    main()