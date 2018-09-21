'''
249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''


def LeetCode249(ary):

    dict={}

    for key in ary:
        tmp=[]
        for i in range(0,len(key)-1):
            diff=ord(key[i+1])-ord(key[i])
            tmp.append(str(diff))

        if len(tmp)>0:
            if ''.join(tmp) in dict.keys():
                dict[''.join(tmp)].append(key)
            else:
                res_lst=[]
                res_lst.append(key)
                dict[''.join(tmp)]=res_lst
        else:
            if str(1) in dict.keys():
                dict[str(1)].append(key)
            else:
                res_lst=[]
                res_lst.append(key)
                dict[str(1)]=res_lst

    return dict


def main():

    ary=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(LeetCode249(ary))

if __name__=='__main__':
    main()