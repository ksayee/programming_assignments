'''

This problem was asked by Twitter.
Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''

def DailyCodingProblem11(str1,ary):

    fnl_lst=[]

    for key in ary:

        try:
            idx=key.index(str1)
        except:
            idx=-1
        if idx==0:
            fnl_lst.append(key)

    return fnl_lst

def main():

    ary=['dog', 'deer', 'deal']
    str1='de'
    print(DailyCodingProblem11(str1,ary))

if __name__=='__main__':
    main()