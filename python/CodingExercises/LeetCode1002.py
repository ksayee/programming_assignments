'''
1002. Find Common Characters
Easy
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
'''


import collections
def LeetCode1002(ary):

    dict=collections.Counter(ary[0])

    for i in range(1,len(ary)):
        word=ary[i]
        tmp_dict=collections.Counter(word)
        for key,val in dict.items():
            if key in tmp_dict.keys() and dict[key]!=0:
                if dict[key]==tmp_dict[key]:
                    pass
                else:
                    dict[key]=abs(dict[key]-tmp_dict[key])
            else:
                dict[key]=0

    lst=[]
    for key, val in dict.items():
        k=0
        while k<val:
            lst.append(key)
            k=k+1
    return lst

def main():

    ary=["bella", "label", "roller"]
    print(LeetCode1002(ary))

    ary = ["cool","lock","cook"]
    print(LeetCode1002(ary))

if __name__=='__main__':
    main()