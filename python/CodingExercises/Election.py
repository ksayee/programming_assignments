# Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.

import collections

def Election(lst):

    dict=collections.Counter(lst)

    fnl={}
    for key,val in dict.items():
        if val in fnl.keys():
            fnl[val].append(key)
        else:
            tmp=[]
            tmp.append(key)
            fnl[val]=tmp

    sort=sorted(fnl.items(),key=lambda x:x[0],reverse=True)[0]

    return sorted(sort[1])[0]

def main():

    lst = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie','john', 'johnny', 'jamie', 'johnny', 'john']
    print(Election(lst))

if __name__ == "__main__":
    main()
