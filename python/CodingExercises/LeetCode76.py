'''
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''

import collections
def LeetCode76(input_str,target):

    i=0
    j=0
    left=0
    right=0
    dict=collections.Counter(target)
    window_dict={}
    while right<len(input_str):
        key=input_str[right]
        if key in dict.keys():
            if key not in window_dict.keys():
                window_dict[key]=1
            else:
                window_dict[key]=window_dict.get(key)+1
        flg=False
        while True:
            if sorted(dict)==sorted(window_dict):
                flg=True
                skey=input_str[left]
                if skey in window_dict.keys():
                    window_dict[skey]=window_dict.get(skey)-1
                    if window_dict[skey]==0:
                        del window_dict[skey]
            else:
                if flg==True:
                    if i==0 and j==0:
                        i=left-1
                        j=right
                    elif right-(left-1)<j-i:
                        i=left-1
                        j=right
                break
            left=left+1
        right=right+1
    return input_str[i:j+1]

def main():

    input_str='abbaacdbcab'
    target='abc'
    print(LeetCode76(input_str,target))

    input_str = 'ADOBECODEBANC'
    target = 'ABC'
    print(LeetCode76(input_str, target))
if __name__=='__main__':
    main()