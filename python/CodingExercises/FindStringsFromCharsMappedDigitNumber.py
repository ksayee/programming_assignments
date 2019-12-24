'''
Find all strings formed from characters mapped to digits of a number
Consider below list where each digit from 1 to 9 maps to few characters.
1 -> ['A', 'B', 'C']
2 -> ['D', 'E', 'F']
3 -> ['G', 'H', 'I']
4 -> ['J', 'K', 'L']
5 -> ['M', 'N', 'O']
6 -> ['P', 'Q', 'R']
7 -> ['S', 'T', 'U']
8 -> ['V', 'W', 'X']
9 -> ['Y', 'Z']
Given a number, replace its digits with corresponding characters in given list and print all strings possible.
Same character should be considered for every occurrence of a digit in the number. Input number is positive and doesn’t contain 0.
Examples :
Input : 121
Output : ADA BDB CDC AEA BEB CEC AFA BFB CFC
Input : 22
Output : DD EE FF
'''

import collections

def Validate(tmp,num,dict):

    for i in range(0,len(num)):
        key=int(num[i])
        if tmp[i] in dict[key]:
            pass
        else:
            return False
    return True

def Combinations_recur(lst,cnt,tmp,fnl_lst,num,dict):

    if len(tmp)==len(num):
        flg=Validate(tmp,num,dict)
        if flg==True:
            fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, num, dict)
        cnt[i]=cnt[i]+1
        tmp.pop()

def FindStringsFromCharsMappedDigitNumber(dict,num):

    base_lst=[]
    for i in range(0,len(num)):
        key=int(num[i])
        if key in dict.keys():
            base_lst.append(''.join(dict[key]))

    base_dict=collections.Counter(''.join(base_lst))
    lst=[]
    cnt=[]
    for key,val in base_dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,num,dict)
    return fnl_lst

def main():
    
    dict={}
    dict[1]=['A', 'B', 'C']
    dict[2] =['D', 'E', 'F']
    dict[3] =['G', 'H', 'I']
    dict[4] =['J', 'K', 'L']
    dict[5] =['M', 'N', 'O']
    dict[6] =['P', 'Q', 'R']
    dict[7] =['S', 'T', 'U']
    dict[8] =['V', 'W', 'X']
    dict[9] =['Y', 'Z']

    num='121'
    print(FindStringsFromCharsMappedDigitNumber(dict,num))

    num = '22'
    print(FindStringsFromCharsMappedDigitNumber(dict,num))

if __name__=='__main__':
    main()