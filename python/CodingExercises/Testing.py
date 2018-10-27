# Find if there is a subarray with 0 sum
# Given an array of positive and negative numbers,
# find if there is a subarray (of size at-least one) with 0 sum.

def AllSubArraySum(ary):

    dict={}
    sum=0
    fnl_lst=[]
    for i in range(0,len(ary)):

        sum=sum+ary[i]

        if sum==0:
            tup=ary[0:i+1]
            fnl_lst.append(tup)
        else:
            if sum in dict.keys():
                tmp=dict[sum]
                for j in tmp:
                    tup=ary[j+1:i+1]
                    fnl_lst.append(tup)
            else:
                tmp=[]
                tmp.append(i)
                dict[sum]=tmp

    return fnl_lst

def Combinations_recur(tmp,fnl_lst,open,close,n):

    if close==n:
        fnl_lst.append(''.join(tmp))
        return

    if open<n:
        tmp.append('{')
        Combinations_recur(tmp, fnl_lst, open+1, close, n)
        tmp.pop()
    if open>close:
        tmp.append('}')
        Combinations_recur(tmp, fnl_lst, open, close+1, n)
        tmp.pop()

def BalancedParenthesesCombinations(n):

    open=0
    close=0
    tmp=[]
    fnl_lst=[]
    Combinations_recur(tmp,fnl_lst,open,close,n)

    return fnl_lst

def BinarySearch(ary, k):

    left=0
    right=len(ary)-1
    flg=False
    while left<right:
        mid=int((left+right)/2)
        if ary[mid]==k:
            flg=True
            break
        if ary[mid]<k:
            left=mid+1
        else:
            right=mid-1
    return flg

def BothHalves(str1):

    mid = len(str1) // 2
    if len(str1)%2==0:
        mid=len(str1)//2
        lst1=str1[:mid]
        lst2=str1[mid:]
    else:
        lst1=str1[:mid]
        lst2=str1[mid+1:]

    if ''.join(sorted(lst1))==''.join(sorted(lst2)):
        return True
    else:
        return False

def CamelCaseSentence(str1):

    lst=str1.split()

    fnl_lst=[]
    for l in lst:
        fnl_lst.append(l.capitalize())
    return ' '.join(fnl_lst)

def ChangeStringCharacter(str,str1):

    lst=list(str)
    fnl_lst=[]
    for i in range(0,len(str1)):

        key=str1[i].lower()
        idx=lst.index(key)
        fnl_lst.append(chr(ord('a')+idx))
    return ''.join(fnl_lst)

def CommonChars(ary):

    lst=[0]*26
    i=1
    for itm in ary:
        tmp=list(itm)
        for l in tmp:
            idx=ord(l)-ord('a')
            if lst[idx]>=i:
                continue
            else:
                lst[idx]=lst[idx]+1
        i=i+1

    fnl_lst=[]
    for i in range(0,len(lst)):
        if lst[i]==len(ary):
            char=ord('a')+i
            fnl_lst.append(chr(char))

    return ''.join(fnl_lst)

def CommonCharacters(s1,s2):

    lst=[0]*26

    fnl_lst=[]
    lst1=list(s1)
    lst2=list(s2)
    for i in range(0,len(lst1)):
        key=lst1[i]
        if key in lst2:
            idx=lst2.index(key)
            del lst2[idx]
            fnl_lst.append(key)

    return ''.join(sorted(fnl_lst))

def ClosestPairsSortedArrays(ary1, ary2, k):

    i=0
    j=len(ary2)-1

    min_diff=999999
    while i<len(ary1) and j>=0:

        sum=ary1[i]+ary2[j]

        diff=abs(k-sum)
        if diff<min_diff:
            idx1=i
            idx2=j
            min_diff=diff

        if sum>k:
            j=j-1
        else:
            i=i+1

    tup=(ary1[idx1],ary2[idx2])

    return tup

def DailyCodingProblem18(ary,k):

    dict={}

    i=0
    max=0
    while i<k:
        if ary[i]>max:
            max=ary[i]
        i=i+1
    tmp=[]
    tmp.append(ary[:k])
    dict[max]=tmp

    for j in range(1,len(ary)):
        max=0
        st=j
        if j+k<=len(ary):
            while j<st+k:
                if ary[j]>max:
                    max=ary[j]
                j=j+1
            if max in dict.keys():
                dict[max].append(ary[st:j])
            else:
                tmp=[]
                tmp.append(ary[st:j])
                dict[max]=tmp
    return dict

def DistinctElementsWindowSizeK(ary, k):

    dict={}

    i=0
    j=k-1

    while j<len(ary):

        tup=ary[i:j+1]
        cnt=len(set(tup))
        if cnt in dict.keys():
            dict[cnt].append(tup)
        else:
            tmp=[]
            tmp.append(tup)
            dict[cnt]=tmp
        i=i+1
        j=j+1

    return dict

def ConsecutiveDuplicates(str1):

    fnl_lst=[]

    for i in range(0,len(str1)):
        key=str1[i]

        if len(fnl_lst)==0:
            fnl_lst.append(key)
        else:
            if fnl_lst[-1]!=key:
                fnl_lst.append(key)
    return ''.join(fnl_lst)

def ConsecutiveOnes(str):

    cnt=0
    max_cnt=0

    flg=False
    for i in range(0,len(str)):

        key=str[i]
        if key=='1':
            flg=True
            cnt=cnt+1
        else:
            if flg==True:
                if cnt>max_cnt:
                    max_cnt=cnt
                flg=False
                cnt=0
    return max_cnt

def ContigousIntegersHashmap(ary):

    dict={}

    for key in ary:
        if key not in dict.keys():
            dict[key]=1

    key=ary[0]
    cnt=0
    while key in dict.keys():
        cnt=cnt+1
        key=key+1
    key=ary[0]-1
    while key in dict.keys():
        cnt=cnt+1
        key=key-1

    if cnt==len(set(ary)):
        return True
    else:
        return False

def FacebookFriends(ary):

    dict={}

    for lst in ary:
        for l in lst:
            if l in dict.keys():
                dict[l]=dict.get(l)+len(lst)-1
            else:
                dict[l]=len(lst)-1
    return dict

def groupanagrams(word_list):

    dict={}
    for word in word_list:

        key=''.join(sorted(word))

        if key in dict.keys():
            dict[key].append(word)
        else:
            tmp=[]
            tmp.append(word)
            dict[key]=tmp

    return dict

def Factorial(n):

    fct=1
    while n!=0:
        fct=fct*n
        n=n-1
    return fct

def FindMissingNumbers(ary):

    ary.sort()
    print(ary)
    fnl_lst=[]
    for i in range(1,len(ary)):

        if ary[i]-ary[i-1]>1:
            tmp=ary[i-1]+1
            while tmp!=ary[i]:
                fnl_lst.append(tmp)
                tmp=tmp+1

    return fnl_lst

def flattenlist(lst):

    fnl_lst=[]

    for l in lst:
        if isinstance(l,list):
            fnl_lst.extend(flattenlist(l))
        else:
            fnl_lst.append(l)
    return fnl_lst

import collections
def GroupMultipleOccurences(ary):

    fnl_lst=[]
    dict=collections.Counter(ary)
    for i in range(0,len(ary)):
        key=ary[i]

        while key in dict.keys() and dict.get(key)>0:
            fnl_lst.append(key)
            dict[key]=dict.get(key)-1
    return fnl_lst

def GroupOccurences(str):

    dict=collections.Counter(str)

    lst=list(str)
    fnl_lst=[]
    for i in range(0,len(lst)):
        key=lst[i]

        while key in dict.keys() and dict.get(key)>0:
            fnl_lst.append(key)
            dict[key]=dict.get(key)-1
    return ''.join(fnl_lst)

def LeadersArray(ary):

    fnl_lst=[]

    max_num=ary[-1]
    for i in range(len(ary)-2,-1,-1):

        key=ary[i]
        if key>max_num:
            fnl_lst.append(key)
            max_num=key

    fnl_lst.reverse()
    return  fnl_lst

def ItinearyTickets(ary):

    dict={}

    for tup in ary:

        dict[tup[0]]=tup[1]

    re_dict={}

    for tup in ary:
        re_dict[tup[1]]=tup[0]

    for key,val in dict.items():

        if key in re_dict.keys():
            continue
        else:
            start=key
            break

    fnl_lst=[]
    while start in dict.keys():
        tmp=(start,dict[start])
        fnl_lst.append(tmp)
        start=dict[start]
    return fnl_lst

def EmployeeManager(ary):

    dict={}
    lst=[]
    for tup in ary:
        emp=tup[0]
        mgr=tup[1]
        lst.append(emp)
        lst.append(mgr)

        if emp!=mgr:
            if mgr not in dict.keys():
                tmp=[]
                tmp.append(emp)
                dict[mgr]=tmp
            else:
                dict[mgr].append(emp)

    lst=list(set(lst))
    fnl_lst=[]

    for itm in lst:
        cnt=0
        if itm in dict.keys():
            cnt=len(dict[itm])+CountEmployees(dict[itm],cnt,dict)
        tup=(itm,cnt)
        fnl_lst.append(tup)

    return fnl_lst


def CountEmployees(val,cnt,dict):

    if len(val)==0:
        return 0
    for l in val:
        if l in dict.keys():
            cnt=len(dict[l])+CountEmployees(dict[l],cnt,dict)
    return cnt

def main():

    #ary = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    #print(AllSubArraySum(ary))

    #n = 3
    #print(BalancedParenthesesCombinations(n))

    #ary = [2, 3, 4, 10, 40]
    #k = 9
    #print(BinarySearch(ary, k))

    #s1 = 'abcaabc'
    #print(BothHalves(s1))

    #str1 = 'I got intern at geeksforgeeks'
    #print(CamelCaseSentence(str1))

    #str = "qwertyuiopasdfghjklzxcvbnm"
    #str1 = "utta"
    #print(ChangeStringCharacter(str, str1))

    #str = "qwertyuiopasdfghjklzxcvbnm"
    #str1 = "egrt"
    #print(ChangeStringCharacter(str, str1))

    #ary = ['geeksforgeeks', 'gemkstones', 'acknowledges', 'aguelikes']
    #print(CommonChars(ary))

    #ary = ['apple', 'orange']
    #print(CommonChars(ary))

    #s1 = 'geeks'
    #s2 = 'forgeeks'
    #print(CommonCharacters(s1, s2))

    #ary1 = [1, 4, 5, 7]
    #ary2 = [10, 20, 30, 40]
    #k = 50
    #print(ClosestPairsSortedArrays(ary1, ary2, k))

    #ary1 = [1, 4, 5, 7]
    #ary2 = [10, 20, 30, 40]
    #k = 32
    #print(ClosestPairsSortedArrays(ary1, ary2, k))

    #ary=[10, 5, 2, 7, 8, 7]
    #k=3
    #print(DailyCodingProblem18(ary, k))

    #ary = [1, 2, 1, 3, 4, 2, 3]
    #k = 4
    #print(DistinctElementsWindowSizeK(ary, k))

    #str1 = 'geeksforgeeks'
    #print(ConsecutiveDuplicates(str1))

    #str = '11000111101010111'
    #print(ConsecutiveOnes(str))

    #ary = [5, 2, 3, 6, 4, 4, 6, 6]
    #print(ContigousIntegersHashmap(ary))

    #ary = [10, 14, 10, 12, 12, 13, 15]
    #print(ContigousIntegersHashmap(ary))

    #ary = [['A', 'B', 'C'], ['B', 'F', 'D'], ['A', 'D'], ['E']]
    #print(FacebookFriends(ary))

    #word_list = ["cat", "dog", "tac", "god", "act", "gdo"]
    #print(groupanagrams(word_list))

    #n = 5
    #print(Factorial(n))

    #ary = [1, 7, 3, 13, 5, 10, 8, 4, 9]
    #print(FindMissingNumbers(ary))

    #lst = [1, [2, 3, 4, 5], 6, 7, [8, 9, [10, 11]]]
    #print(flattenlist(lst))

    #ary = [5, 3, 5, 1, 3, 3]
    #print(GroupMultipleOccurences(ary))

    #ary = [4, 6, 9, 2, 3, 4, 9, 6, 10, 4]
    #print(GroupMultipleOccurences(ary))

    #str = 'geeksforgeeks'
    #print(GroupOccurences(str))

    #str = 'occurrence'
    #print(GroupOccurences(str))

    #str = 'cdab'
    #print(GroupOccurences(str))

    #ary = [16, 17, 4, 3, 5, 2]
    #print(LeadersArray(ary))

    #ary = [("Chennai", "Banglore"), ("Bombay", "Delhi"), ("Goa", "Chennai"), ("Delhi", "Goa")]
    #print(ItinearyTickets(ary))

    ary = [('A', 'C'), ('B', 'C'), ('C', 'F'), ('D', 'E'), ('E', 'F'), ('F', 'F'), ('G', 'A')]
    print(EmployeeManager(ary))


if __name__=='__main__':
    main()