
def Anagram(str1,str2):

    if len(str1)!=len(str2):
        return False
    elif ''.join(sorted(str1))==''.join(sorted(str2)):
        return True
    else:
        return False

def StructureString(str):

    lst=str.split()
    print(' '.join(lst))

def UniqueNumber(n):

    lst={}
    while(n!=0):
        key=n%10
        if key in lst.keys():
            return False
        else:
            lst[key]=1
        n=int(n/10)
    return True

def UniqueChar(str1):
    lst=[]

    for i in range(0,len(str1)):
        key=str1[i]
        lst.append(key)

    if len(lst)==len(set(lst)):
        return True
    else:
        return False

def UnionIntersection(lst1,lst2):

    print(list(set(lst1).union(set(lst2))))
    print(list(set(lst1).intersection(set(lst2))))

def SubsetArray(ary1,ary2):

    big_lst=[]
    sml_lst=[]
    if len(ary1)>len(ary2):
        big_lst=ary1
        sml_lst=ary2
    else:
        big_lst = ary2
        sml_lst = ary1

    dict={}
    for i in range(0,len(big_lst)):
        key=big_lst[i]

        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    for i in range(0,len(sml_lst)):
        key=sml_lst[i]

        if key in dict.keys() and dict.get(key)>0:
            dict[key]=dict.get(key)-1
        else:
            return False

    return True

def StringPalindrome(str1):

    st=0
    end=len(str1)-1

    while st<end:
        if str1[st]!=str1[end]:
            return False
        else:
            st=st+1
            end=end-1
    return True

def StringExpansion(str1):

    fnl_lst=[]
    prev_char=''
    print(str1)
    for i in range(0,len(str1)):
        if ord(str1[i])>=48 and ord(str1[i])<=57:
            tmp_cnt=int(str1[i])
            while tmp_cnt>0:
                fnl_lst.append(prev_char)
                tmp_cnt=tmp_cnt-1

        prev_char=str1[i]
    return ''.join(fnl_lst)

def StringCompression(str1):

    fnl_lst=[]
    print(str1)
    prev_char=str1[0]
    cnt=1
    for i in range(1,len(str1)):
        if prev_char==str1[i]:
            cnt=cnt+1
        else:
            fnl_lst.append(prev_char)
            fnl_lst.append(str(cnt))
            cnt=1
        prev_char=str1[i]
    fnl_lst.append(prev_char)
    fnl_lst.append(str(cnt))
    return ''.join(fnl_lst)

def SingleOccurence(ary):

    print(ary)
    fnl_lst=[]

    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[i+1:] and key not in ary[:i]:
            fnl_lst.append(key)
    return fnl_lst

def SecondMax(ary):

    max=ary[0]
    sec_max=ary[0]
    print(ary)
    for i in range(1,len(ary)):
        if ary[i]>max:
            sec_max=max
            max=ary[i]
        elif ary[i]>sec_max:
            sec_max=ary[i]
    return sec_max

def ReverseWords(str1):

    print(str1)
    lst=str1.split()
    print(lst)
    fnl_lst=[]

    for i in range(0,len(lst)):
        key=lst[i]
        fnl_lst.append(''.join(reversed(key)))
    return ' '.join(fnl_lst)

def ReverseNumber(n):

    found=False
    fnl_lst=[]
    while(n!=0):
        key=n%10
        if key==0 and found==False:
            n=int(n/10)
            continue
        else:
            fnl_lst.append(str(key))
            found=True
        n=int(n/10)
    return ''.join(fnl_lst)

def ReverseAry(ary):

    st=0
    end=len(ary)-1

    while(st<end):
        tmp=ary[st]
        ary[st]=ary[end]
        ary[end]=st
        st=st+1
        end=end-1
    return ary

def ReplaceString(tmp_str):

    print(tmp_str)
    lst=tmp_str.split('$')
    found=False
    fnl_lst=[]
    for i in range(0,len(lst)):
        if lst[i]=='' and found==False:
            continue
        elif lst[i]!='' and found==False:
            found=True
            fnl_lst.append(lst[i])
        elif lst[i]=='' and found==True:
            continue
        else:
            fnl_lst.append('%20')
            fnl_lst.append(lst[i])
    return ''.join(fnl_lst)

def RemoveDuplicates(ary):

    print(ary)
    fnl_lst=[]

    for i in range(0,len(ary)):
        key=ary[i]
        if key not in fnl_lst:
            fnl_lst.append(key)
    return fnl_lst

def PlusOne(ary,n):
    print(ary)
    print(n)

    val=n
    carry=0
    fnl_lst=[]
    for i in range(len(ary)-1,-1,-1):
        val=val+ary[i]+carry
        fnl_lst.append(str(val%10))
        carry=int(val/10)
        val=0
    if carry>0:
        fnl_lst.append(str(carry))

    print(fnl_lst)
    return ''.join(reversed(fnl_lst))

def OddPosition(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):
        if i%2==0:
            continue
        else:
            fnl_lst.append(ary[i])
    return fnl_lst

def EvenPosition(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):
        if i%2==0:
            fnl_lst.append(ary[i])
    return fnl_lst

def NumberPalindrome(n):

    print(n)
    tmp_num=n
    fnl_lst=[]
    while tmp_num!=0:
        fnl_lst.append(str(tmp_num%10))
        tmp_num=int(tmp_num/10)

    if ''.join(fnl_lst)==str(n):
        return True
    else:
        return False

def MostRecurringElement(ary):
    print(ary)

    lst={}
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1
    max_key=0
    max_val=-9999
    for key,value in lst.items():
        if value>max_val:
            max_key=key
            max_val=value
    return max_key,max_val

def MinAbsDiff(ary):
    print(ary)

    ary.sort()
    print(ary)

    min_abs=9999
    for i in range(1,len(ary)):
        if abs(ary[i]-ary[i-1])<min_abs:
            min_abs=abs(ary[i]-ary[i-1])
    return min_abs

def Median(ary):
    ary.sort()
    print(ary)

    length=len(ary)
    if length%2!=0:
        med=ary[int(length/2)]
    else:
        num1=ary[(int(length/2))-1]
        num2=ary[int((length/2))]
        med=(num1+num2)/2
    return med

def AddingNumber(n):

    print(n)
    sum=0

    while n>9:
        tmp=n
        sum=0
        while tmp!=0:
            sum=sum+tmp%10
            tmp=int(tmp/10)
        n=sum
    return sum

def AddingTwoNumbers(num1,num2):

    print(num1,num2)


    if num1>num2:
        big_num=num1
        sml_num=num2
    else:
        big_num=num2
        sml_num=num1

    carry=0
    fnl_lst=[]
    while big_num!=0:
        if sml_num!=0:
            val=big_num%10+sml_num%10+carry
            sml_num=int(sml_num/10)
        else:
            val=big_num%10+carry
        big_num=int(big_num/10)

        carry=int(val/10)
        fnl_lst.append(str(val%10))

    if carry>0:
        fnl_lst.append(str(carry))

    return ''.join(reversed(fnl_lst))

def Fibonaci(n):

    fnl_lst=[]
    fnl_lst.append(0)
    fnl_lst.append(1)
    i=2
    while i<=n-2:
        key=fnl_lst[i-1]+fnl_lst[i-2]
        fnl_lst.append(key)
        i=i+1
    return fnl_lst

def CummulativeSum(ary):

    fnl_lst=[]
    sum=0
    for i in range(0,len(ary)):
        sum=sum+ary[i]
        fnl_lst.append(sum)
    return fnl_lst

def ReplaceNone(str):

    print(str)
    lst=str.split()
    print(lst)
    fnl_lst=[]
    for i in range(0,len(lst)):
        if i==0:
            fnl_lst.append(lst[i])
        else:
            fnl_lst.append('NONE')
            fnl_lst.append(lst[i])
    return ''.join(fnl_lst)

def IPaddress(str):

    print(str)
    lst=str.split('.')

    if len(lst)!=4:
        return False
    else:
        for i in range(0,len(lst)):
            try:
                if int(lst[i])>=0 and int(lst[i])<=255:
                    continue
                else:
                    return False
            except:
                return False
    return True

def Percentile(ary,n):

    ln=len(ary)-1

    for i in range(0,len(ary)):

        if i/ln<n:
            continue
        else:
            break

    return ary[i]

def UniqueDigits(n):

    lst={}

    while n!=0:
        key=n%10

        if key in lst.keys():
            return False
        else:
            lst[key]=1
        n=int(n/10)
    return True

import random

def fnl(i):
    return random.random()

def ReturnRandom(ary,n):

    return sorted(ary, key=fnl)[:5]

def CheckSubstring(str,sub_str):

    if str.count(sub_str)>0:
        return True
    else:
        return False

def MovieTimes(tup_list):

    print(tup_list)

    sort_list=sorted(tup_list,key=lambda x:x[0])
    print(sort_list)
    fnl_tup=[]
    fnl_tup.append(sort_list[0])
    k=0

    for i in range(1,len(sort_list)):


        if sort_list[i][0]<fnl_tup[k][1] and sort_list[i][1]>fnl_tup[k][1]:
            tmp_tup=(fnl_tup[k][0],sort_list[i][1])
            del fnl_tup[k]
            fnl_tup.append(tmp_tup)
        elif sort_list[i][0]<fnl_tup[k][1] and sort_list[i][1]<fnl_tup[k][1]:
            continue
        elif sort_list[i][0]>fnl_tup[k][1]:
            k=k+1
            fnl_tup.append(sort_list[i])
    sum=0
    for i in range(0,len(fnl_tup)):

        sum=sum+fnl_tup[i][1]-fnl_tup[i][0]
    return sum

def MovieTimesAct(tup_list):

    print(tup_list)

    sort_list=sorted(tup_list,key=lambda x:x[0])
    print(sort_list)

    fnl_lst=[]
    fnl_lst.append(sort_list[0])
    k=0

    for i in range(1,len(sort_list)):

        if fnl_lst[k][1]>sort_list[i][0]:
            tmp_lst=(fnl_lst[k][0],sort_list[i][1])
            del fnl_lst[k]
            fnl_lst.append(tmp_lst)
        else:
            k=k+1
            fnl_lst.append(sort_list[i])
    print(fnl_lst)

    sum=0
    for i in range(0,len(fnl_lst)):
        sum=sum+fnl_lst[i][1]-fnl_lst[i][0]

    return sum

def ReturnNewString(str):

    new_str=''
    if str.find('bad')>str.find('not'):

        new_str=str[:str.find('not')]+'good'+str[str.find('bad')+3:]
        return new_str
    else:
        return str


import collections
import re

def Top5Words(path):

    f=open(path,'r')
    data=f.read()
    words=re.split(r'\s',data)
    fnl_lst=[]
    for word in words:
        if word=='':
            continue
        else:
            fnl_lst.append(word)
    c=list(collections.Counter(fnl_lst).elements())
    print(c)

    return collections.Counter(fnl_lst).most_common(5)

def FlattenList(lst):
    out_lst=[]

    for i in lst:
        if isinstance(i,(list,tuple)):
            out_lst.extend(FlattenList(i))
        else:
            out_lst.append(i)
    return out_lst

def IPvalidate(ip):

    lst=ip.split('.')
    if len(lst)!=4:
        return False
    else:
        for i in range(0,len(lst)):

            try:
                key=int(lst[i])
                if key>=0 and key<=255:
                    continue
                else:
                    return False
            except:
                return False
    return True

def FlattenListKS(lst):
    out_lst=[]

    for l in lst:
        if isinstance(l,(list,tuple)):
            out_lst.extend(FlattenListKS(l))
        else:
            out_lst.append(l)
    return out_lst

def mostFrequent(lst):

    return collections.Counter(lst).most_common(1)[0][0]

def firstNonRecurring(lst):

    for i in range(0,len(lst)):
        key=lst[i]
        if key not in lst[i+1:] and key not in lst[:i]:
            return key

def DoGCD(sml_num,big_num):

    while big_num%sml_num!=0:
        rem=big_num%sml_num
        big_num=sml_num
        sml_num=rem

    return sml_num

def GCD(ary):

    ary.sort()
    sml_num=ary[0]

    i=1
    while i<len(ary):
        sml_num=DoGCD(sml_num,ary[i])
        i=i+1
    return sml_num

def LCM(ary):

    ary.sort()
    sml_num=ary[0]
    i=1
    while i<len(ary):
        gcd=DoGCD(sml_num,ary[i])
        lcm=int((sml_num*ary[i])/gcd)
        sml_num=lcm
        i=i+1
    return lcm

def ABS(ary):

    min_abs=9999

    ary.sort()

    for i in range(1,len(ary)):
        min=ary[i]-ary[i-1]
        if min<min_abs:
            min_abs=min

    return min_abs

def MED(ary):

    ary.sort()
    if len(ary)%2!=0:
        idx=int(len(ary)/2)
        return ary[idx]
    else:
        idx1=int(len(ary)/2)
        idx2 = int(len(ary) / 2)-1
        num=(ary[idx1]+ary[idx2])/2
        return num

def Digits(num):

    lst=[]

    while num!=0:
        rem=num%10
        lst.append(rem)
        num=int(num/10)

    lst.reverse()
    return lst

def OddElements(ary):

    lst=[]
    for i in range(0,len(ary)):
        if i%2!=0:
            lst.append(ary[i])

    return lst

def EmplDict(lst):

    dict={}

    for i in range(0,len(lst)):
        if len(lst[i])>1:
            tmp1=lst[i][0]
            tmp2=lst[i][1]
        else:
            tmp1=lst[i][0]
            tmp2=''

        if tmp1 in dict.keys() and tmp2!='':
            dict[tmp1]=dict.get(tmp1)+1
        elif tmp1 in dict.keys() and tmp2=='':
            continue
        elif tmp1 not in dict.keys() and tmp2!='':
            dict[tmp1]=1
        elif tmp1 not in dict.keys() and tmp2=='':
            dict[tmp1]=0

        if tmp2!='':
            if tmp2 in dict.keys():
                dict[tmp2]=dict.get(tmp2)+1
            else:
                dict[tmp2]=1

    return dict

def EmplDictSmp(lst):

    dict={}
    print(lst)
    for i in range(0,len(lst)):

        for j in range(0,len(lst[i])):
            key=lst[i][j]
            if key in dict.keys():
                dict[key]=dict.get(key)+len(lst[i])-1
            else:
                dict[key]=len(lst[i])-1
    return dict

def main():

    #str1='MARY'
    #str2='ARMY'
    #print(Anagram(str1,str2))
    #print(''.join(sorted(str1))==''.join(sorted(str2)))

    #str= '       I work          in Amazon in Seattle       I           life         '
    #StructureString(str)

    #n=1000
    #print(UniqueNumber(n))

    #str1='marya'
    #print(list(set(sorted(str1))))
    #print(UniqueChar(str1))

    #lst1 = [1, 3, 4,3, 5, 7,5]
    #lst2 = [2, 3, 5, 6,5]
    #UnionIntersection(lst1,lst2)

    #ary1 = [11, 1, 13, 21, 3, 7,1]
    #ary2 = [11,3, 7, 1,1]

    #print(SubsetArray(ary1, ary2))

    #str1 = 'malayalam'
    #print(StringPalindrome(str1))

    #str1 = 'a3b1c5a2'
    #print(StringExpansion(str1))
    '''
    fnl=[]
    for i in range(0,len(str1)):
        if str1[i]>='0' and str1[i]<='9':
            cnt=int(str1[i])
            while cnt!=0:
                fnl.append(prev_chr)
                cnt=cnt-1
        else:
            prev_chr=str1[i]
    print(''.join(fnl))
    '''

    #str1 = 'aabcccccaa'
    #print(StringCompression(str1))

    #ary = [1, 2, 2, 2, 3, 4, 56, 3, 3, 3, 7, 9, 4, 9, 4, 85, 6, 34, 6, 1, 10, 34, 45]
    #print(SingleOccurence(ary))

    #ary = [5, 89,89,89, 20, 64, 20, 45,64,64,64, 53]
    #print(sorted(set(ary),reverse=True)[1])
    #print(SecondMax(ary))

    #str1 = 'I am using hackerrank to improve programming'
    '''
    lst=str1.split()
    fnl=[]
    for i in range(0,len(lst)):
        key=''.join(reversed(lst[i]))
        fnl.append(key)
    print(' '.join(fnl))
    '''
    #print(ReverseWords(str1))

    #n= 340500
    #print(ReverseNumber(n))

    #ary = [1, 2, 3, 4, 5, 6, 7]
    #ary.reverse()
    #print(ary)
    #print(ReverseAry(ary))

    #str1 = '$$$$$Mr$$John$Smith$$$$$$'
    #str2 = 'Mr$$John$Smith'
    #str3 = '$$$$$Mr$$John$Smith'
    #str4 = '$$$$$Mr$$John$$$$Smith$'
    #print(ReplaceString(str1))
    #print(ReplaceString(str2))
    #print(ReplaceString(str3))
    #print(ReplaceString(str4))

    #ary = [1, 1, 1, 2, 2, 3, 5, 5, 7, 7, 7, 8, 9, 10, 34, 34, 56, 56, 56]
    #print(RemoveDuplicates(ary))

    #ary = [9, 9, 9, 7]
    #n = 9
    #print(PlusOne(ary, n))

    #ary = [0, 1, 2, 3, 4, 5]
    #print(OddPosition(ary))

    #ary = [1, -1, 2, -2, 5, 8, 9]
    #print(EvenPosition(ary))

    #num = 112211
    #print(NumberPalindrome(num))
    #num = 3344882
    #print(NumberPalindrome(num))
    '''
    ary = [4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1]
    lst=collections.Counter(ary).most_common()
    print(lst)
    tst=list(filter(lambda x:x[1]>1,lst))
    print(tst)
    '''

    #tup=(1,2,3,4,5,6,7,8,9,10)
    #lst=list(reversed(tup))
    #print(lst)
    #print(tup[:-1])
    '''
    lst=[(1,2), (3,4), (8,9)]
    out_lst=[]
    for l in lst:
        if isinstance(l,tuple):
            out_lst.extend(l)
        else:
            out_lst.append(l)
    print(tuple(out_lst))
    '''
    #lst=[1,2,3,4,5]
    #print(lst.index(3))
    #del lst[2]
    #print(lst)
    '''
    ary = (4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1)
    lst=collections.Counter(ary).most_common()
    print(collections.Counter(ary).most_common())
    print(list(filter(lambda x:x[1]>1,lst)))
    '''
    #tup=('a','a','a','a','a','a',)
    #print(''.join(tup))

    #color_dict = {'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
    #print(sorted(color_dict.items(),key=lambda x:x[0]))

    #str1='w3resource'
    #print(dict(collections.Counter(str1)))

    #lst=[11, 33, 50]
    #print(''.join(map(str,lst)))

    #lst1=['a','b','c','d','e','f']
    #lst2=['d','e','f','g','h']

    #print(list(set(lst1).difference(set(lst2))))
    #print(list(set(lst2).difference(set(lst1))))

    #dict=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
    #print(sorted(dict,key=lambda x:x['key']['subkey'], reverse=True))

    #lst1=["red", "orange", "green", "blue", "white"]
    #lst2=["black", "yellow", "green", "blue"]

    #print(list(set(lst1).difference(lst2)))
    #print(list(set(lst2).difference(lst1)))

    #lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    #print(max(lst,key=lambda x:sum(x)))

    #lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    '''
    fnl=[]
    for i in range(0,len(lst)):
        key=lst[i]
        if key in lst[i+1:] or key in lst[:i]:
            continue
        else:
            fnl.append(lst[i])
    print(fnl)
    '''
    '''
    fnl=[]
    for i in range(0,len(lst)):
        key=lst[i]
        if key not in fnl:
            fnl.append(key)
    print(fnl)
    '''
    '''
    lst= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

    cnt=1
    fnl=[]
    print(lst)
    tmp=[]
    for i in range(0,len(lst)):
        if cnt==1:
            tmp=[]
            tmp.append(lst[i])

        else:
            tmp.append(lst[i])
        cnt=cnt+1
        if cnt==6:
            cnt=1
            fnl.append(tmp)
    if len(tmp)<6:
        fnl.append(tmp)

    print(fnl)
    '''
    '''
    lst=['p', 'q']
    n=5
    fnl=[]

    cnt=1
    while cnt<=n:
        for i in range(0,len(lst)):
            key=lst[i]+str(cnt)
            fnl.append(key)
        cnt=cnt+1
    print(fnl)
    '''

    #lst1=["Red", "Green", "Orange", "White"]
    #lst2=["Black", "Green", "White", "Pink"]
    #print(list(set(lst1).intersection(set(lst2))))

    #dict={'x':500, 'y':5874, 'z': 560}
    #print(max(dict.items(),key=lambda x:x[1])[1])
    #print(min(dict.items(), key=lambda x: x[1])[1])

    '''
    lst=[("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
    dict={}

    for i in range(0,len(lst)):
        key=lst[i][0]
        if key in dict.keys():
            dict[key].append(lst[i][1])
        else:
            dict[key]=[]
            dict[key].append(lst[i][1])
    print(dict)
    '''
    '''
    print(lst)
    fnl_lst=[]
    for i in range(0,len(lst)):
        if lst[i][1]>1:
            fnl_lst.append(lst[i])
    print(fnl_lst)
    '''

    #print(MostRecurringElement(ary))
    #print(collections.Counter(ary).most_common(1)[0][0])

    #ary = [30, 5, 20, 9]
    #print(MinAbsDiff(ary))

    #ary1 = [5, 89, 20, 64, 20, 45]
    #print(Median(ary1))

    #ary1 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    #print(Median(ary1))

    '''
    ary1.sort()
    print(ary1)

    if len(ary1)%2!=0:
        i=int(len(ary1)/2)
        print(ary1[i])
    else:
        ind1=int(len(ary1)/2)
        ind2=int(len(ary1)/2)-1
        med=(ary1[ind1]+ary1[ind2])/2
        print(med)
    '''
    '''
    num=679
    while num>9:
        sum=0
        tmp=num
        while tmp!=0:
            sum=sum+tmp%10
            tmp=int(tmp/10)
        num=sum
    print(sum)
    '''
    '''
    fnl=[]
    fnl.append(0)
    fnl.append(1)
    cnt=2
    i=1
    while cnt!=23:
        fnl.append(fnl[i-1]+fnl[i])
        i=i+1
        cnt=cnt+1
    print(fnl)
    '''

    #num = 38
    #print(AddingNumber(num))

    #num = 679
    #print(AddingNumber(num))

    #num1 = 37
    #num2 = 679
    #print(AddingTwoNumbers(num1,num2))

    #n = 20
    #print(Fibonaci(n))

    #ary = [1, 1, 1]
    #print(CummulativeSum(ary))

    #ary = [1, -1, 3]
    #print(CummulativeSum(ary))

    #str = "          Amazon is a     fun place to    fun work and        is     very      fun to be    "
    #print(ReplaceNone(str))

    #ip = '69.89.18.226'
    #print(IPaddress(ip))

    #ip='69.89.345.226'
    #print(IPaddress(ip))

    #ip = '69.89.345'
    #print(IPaddress(ip))

    #ip = '69.89.345.aa'
    #print(IPaddress(ip))

    #ary = [5, 89, 20, 64, 20, 45]
    #n = 0.75

    #print(Percentile(ary, n))

    #ary = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    #n = 0.9
    #print(Percentile(ary, n))

    #n=4592
    #print(UniqueDigits(n))

    #n=1998
    #print(UniqueDigits(n))

    #ary=[1,2,3,4,5,6,7,8,9]
    #n=5
    #print(ReturnRandom(ary,n))

    #str = 'aabbccabab'
    #sub_str='ab'
    #print(CheckSubstring(str,sub_str))

    #tup_list = [(0, 15), (20, 25), (40, 50), (10, 30), (45, 54), (55, 65)]
    #print(MovieTimes(tup_list))

    #tup_list = [(0, 15), (40, 50), (10, 30), (45, 54), (55, 65)]
    #print(MovieTimesAct(tup_list))

    '''
    sort_tup_list=sorted(tup_list,key=lambda x:x[0])
    print(sort_tup_list)

    fnl_tup=[]

    fnl_tup.append(sort_tup_list[0])
    k=0

    for i in range(1,len(sort_tup_list)):
        if sort_tup_list[i][0]<tup_list[k][1]:
            if sort_tup_list[i][1]<tup_list[k][1]:
                continue
            else:
                tmp_tup=(tup_list[k][0],sort_tup_list[i][1])
                del fnl_tup[k]
                fnl_tup.append(tmp_tup)
        else:
            k=k+1
            fnl_tup.append(sort_tup_list[i])
    print(fnl_tup)

    sum=0
    for i in range(0,len(fnl_tup)):
        sum=sum+fnl_tup[i][1]-fnl_tup[i][0]
    print(sum)
    '''

    #tup=(tup_list[0][0],tup_list[1][1])
    #print(tup)

    #def fnl(ary):
    #    return ary[-1]

    #ary = ['xy', 'bc', 'ur', 'aa', 'il']
    #print(ary)
    #print(sorted(ary, key=fnl,reverse=True))
    #print(sorted(ary, key=str.lower))

    #str='spring'
    #print(str[:2]+str[-2:])

    #str='babble'
    #print(str.replace('b','*'))

    #str='This movie is not so bad!!'
    #print(ReturnNewString(str))

    #str = 'This dinner is not that bad!'
    #print(ReturnNewString(str))

    #str = 'This tea is not hot'
    #print(ReturnNewString(str))

    #str = "It's bad yet not"
    #print(ReturnNewString(str))

    #path = '/Users/kartiksayee/Downloads/hamlet.txt'
    #print(Top5Words(path))

    #str='abracadabra'
    #print(collections.Counter(str).most_common(3))

    #str='this is kartik working in amazon is expedia sayee this kartik a will working'
    #print(collections.Counter(str.split()).most_common(3))

    #tup=(1,2,'kartik')
    #print(tup)

    #tup=(2, 4, 5, 6, 2, 3, 4, 4, 7 )
    #lst=list(tup)
    #rev=reversed(tup)
    #print(list(rev))
    #print(collections.Counter(tup).most_common(2))
    '''
    lst=[("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
    dict={}

    for i in range(0,len(lst)):
        key=lst[i][0]
        if key in dict.keys():
            dict[key].append(lst[i][1])
        else:
            dict[key]=[]
            dict[key].append(lst[i][1])
    print(dict)
    '''

    #lst=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    #fnl_lst=[]
    '''
    for i in range(0,len(lst)):
        tmp=tuple(lst[i][:-1])+(100,)
        fnl_lst.append(tmp)

    print(fnl_lst)
    '''
    #lst=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    #fnl_lst=[]
    '''
    for i in range(0,len(lst)):
        if len(lst[i])==0:
            continue
        else:
            fnl_lst.append(lst[i])
    print(fnl_lst)
    '''

    #lst=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

    #print(sorted(lst,key=lambda x:x[1], reverse=True))

    #d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    #print(sorted(d.items(),key=lambda x:x[1], reverse=True))

    #dic1 = {1: 10, 2: 20}
    #dic2 = {3: 30, 4: 40}
    #dic3 = {5: 50, 1: 60}
    #inp=[dic1,dic2,dic3]
    #print(inp)
    #fnl={}
    '''
    for i in range(0,len(inp)):
        tmp=inp[i]
        for key,val in tmp.items():
            if key in fnl.keys():
                fnl[key]=fnl.get(key)+val
            else:
                fnl[key]=val
    print(fnl)
    '''
    #fnl={}
    #for i in range(1,16):
    #    fnl[i]=i*i
    #print(fnl)
    '''
    color_dict = {'red': '#FF0000',
                  'green': '#008000',
                  'black': '#000000',
                  'white': '#FFFFFF'}
    print(color_dict)
    print(sorted(color_dict.items(),key=lambda x:x[0]))
    '''

    #lst={'x': 500, 'y': 5874, 'z': 560}
    #print(sorted(lst.items(),key=lambda x:x[1],reverse=True)[0][1])
    #print(max(lst.items(),key=lambda x:x[1])[1])
    #print(sorted(lst.items(), key=lambda x: x[1])[0][1])
    #print(min(lst.items(),key=lambda x:x[1])[1])

    #lst={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
    #print(lst)
    #print(collections.Counter(lst).most_common(3))
    #print(sorted(lst.items(),key=lambda x:x[1],reverse=True)[:3])

    '''
    lst={'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    print(lst)
    fnl={}

    for key, val in lst.items():
        tmp=list(sorted(val))
        fnl[key]=tmp
    print(fnl)
    '''
    #lst1 = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

    #print(sorted(lst1.items(),key=lambda x:sum(x[1]),reverse=True))
    str='w3resource'
    #print(sorted(dict(collections.Counter(str1).most_common()).items(),key=lambda x:x[1],reverse=True))
    #dict={}
    '''
    for i in range(0,len(str)):
        key=str[i]
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1
    print(dict)
    '''
    '''
    lst=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    print(lst)
    fnl={}
    for i in range(0,len(lst)):
        tmp=lst[i]
        fnl[tmp['item']]=fnl[tmp['item']]+tmp['amount']
    print(fnl)
    '''
    '''
    lst=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    fnl=[]
    for i in range(0,len(lst)):

        for key,val in lst[i].items():
            fnl.append(val)
    print(set(fnl))
    '''
    #print(len({'a':1,'b':2}))
    '''
    lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    fnl=[]
    for i in range(0,len(lst)):
        if lst[i] not in fnl:
            fnl.append(lst[i])
    print(fnl)
    '''
    #lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    #print(sorted(lst,key=lambda x:sum(x),reverse=True)[0])
    '''
    pi = 22 / 7
    str1 = str(pi)
    fnl = []
    cnt = 0
    for i in range(0, len(str1)):
        if str1[i] == '.':
            continue
        else:
            fnl.append(int(str1[i]))
            cnt = cnt + 1
        if cnt == 3:
            break
    print(fnl)
    #print(max(lst, key=sum))
    '''
    '''
    dict={}
    for i in range(0,len(lst)):
        dict[''.join(str(lst[i]))]=sum(lst[i])
    print(dict)
    print(max(dict.items(),key=lambda x:x[1])[0])
    '''
    #lst=[10,11,12]
    #print(min(lst))

    #lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    #print(sorted(lst,key=lambda x:x[1]))

    #lst=[10,20,30,20,10,50,60,40,80,50,40]
    #print(list(set(lst)))

    #lst1=[1,2,3,4]
    #print(lst1.index(3))
    #lst2=[1,2,5]
    #print(set(lst1)-set(lst2))

    #lst=[[2,4,3],[1,5,6], [9], [7,9,0]]
    #fnl=[]
    #for i in range(0,len(lst)):
    #    fnl.extend(lst[i])
    #print(fnl)

    
    '''
    lst=[1,2,3,4,5,6,7,8,9]
    import random

    def fnl(i):
        return random.random()

    print(sorted(lst,key=fnl)[:5])
    print(random.randrange(10,100,5))
    '''
    #lst= [10,10,10,10,20,20,20,20,40,40,50,50,30]
    #print(collections.Counter(lst).most_common(2))

    '''
    lst=['p', 'q']
    n=5
    i=1
    fnl=[]
    while i<=5:
        for j in range(0,len(lst)):
            str1=lst[j]+str(i)
            fnl.append(str1)
        i=i+1
    print(fnl)
    '''
    '''
    lst=[0,1,2,3,4,5]
    fnl=[]
    for i in range(0,len(lst)):
        if i%2==0:
            continue
        else:
            fnl.append(lst[i])
            fnl.append(lst[i-1])
    print(fnl)
    '''
    '''
    lst=[11, 33, 50]
    fnl_str=''
    for i in range(0,len(lst)):
        fnl_str=fnl_str+str(lst[i])
    print(fnl_str)
    '''
    '''
    lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    n=5
    cnt=1
    fnl=[]
    tmp=[]
    for i in range(0,len(lst)):
        if cnt==n or i+1==len(lst):
            if i<cnt:
                k=0
            else:
                k=i-cnt+1
            tmp=list(lst[k:i+1])
            cnt=0
            fnl.append(tmp)
        cnt=cnt+1

    print(fnl)
    '''
    #lst=[(4, 1), (1, 2), (6, 0)]
    #print(sorted (lst,key=lambda x:x[1]))

    '''
    lst=['abc', 'xyz', 'aba', '1221']
    cnt=0
    for i in range(0,len(lst)):
        if len(lst[i])>=2 and lst[i][0]==lst[i][-1]:
            cnt=cnt+1
    print(cnt)
    '''

    #lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    #print(sorted(lst,key=lambda x:x[1]))

    ''''
    import random
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(color)
    random.shuffle(color)
    print(color)
    '''
    '''
    lst1=[1, 2, 3, 4]
    lst2=[1, 2]
    print(list(set(lst1)-set(lst2)))
    print(lst1.index(4))
    '''
    #color = [1,2,3,4]
    #print(''.join(str(color)))

    ''''
    lst=[[2,4,3],[1,5,6], [9], [7,9,0]]
    fnl=[]
    for i in range(0,len(lst)):
        fnl.extend(lst[i])
    print(fnl)
    '''
    '''
    lst = [10, 23, 3, 4]
    min=999
    sec_min=999
    for i in range(0,len(lst)):
        if lst[i]<min:
            sec_min=min
            min=lst[i]
        elif lst[i]<sec_min:
            sec_min=lst[i]
    print(sec_min)
    '''
    '''
    lst=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
    fnl=[]
    for l in lst:
        fnl.extend(l)
    print(list(set(fnl)))
    '''
    '''
    dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    dict1=dict
    print(dict1)
    print(sorted(dict.items(), key=lambda x:x[1]))
    '''
    #lst=[1,2,3,4]
    #lst.reverse()
    #print(lst)

    '''
    lst=[1, 3, 5, 3, 7, 1, 9, 3]
    print(lst)
    for i in range(0,len(lst)):
        if lst[i]==3:
            del lst[i]
            break
    print(lst)
    '''
    '''

    n1=54
    n2=144

    if n1>n2:
        sml_num=n2
        big_num=n1
    else:
        sml_num=n1
        big_num=n2

    while(big_num%sml_num!=0):
        rem=big_num%sml_num
        big_num=sml_num
        sml_num=rem
    print(sml_num)
    '''
    '''
    n=898

    while n>9:
        tmp=n
        sum=0
        while(tmp!=0):
            sum=sum+tmp%10
            tmp=int(tmp/10)

        n=sum
    print(n)
    print(ord('n'))
    '''
    '''
    ip='69.89.18.226'
    print(IPvalidate(ip))

    ip='69.89.345.226'
    print(IPvalidate(ip))

    ip = '69.89.345'
    print(IPvalidate(ip))

    ip = '69.89.345.aa'
    print(IPvalidate(ip))
    '''

    #print(mostFrequent([0, 1, 4, 4, 3]))
    #print(mostFrequent([1, 0, 2, 2, 1, 2, 1, 1]))
    #print(mostFrequent([1, 2, 2, 3, 1, 2, 2, 1]))

    #print(firstNonRecurring([1, 2, 1]))
    #print(firstNonRecurring([1, 2, 1, 3, 2]))
    #print(firstNonRecurring([1, 2, 1, 3, 3, 4]))
    #print(firstNonRecurring([1, 2, 1, 2]))

    #print(GCD([12,18,30]))
    #print(GCD([12,21,30]))
    #print(GCD([23,17,89]))

    #print(LCM([12,24,36]))
    #print(LCM([2,3,5]))
    #print(LCM([2,4,3]))
    #print(LCM([2,3,7]))

    #print(ABS([1,2,3,4,4,5]))
    #print(ABS([1,-2,3,-4,4,-5]))
    #print(ABS([30,15,21,17,24,5]))

    #print(MED([1, 5, 2]))
    #print(MED([-5, -1, -3]))
    #print(MED([8, 2, 7,  6]))

    #print(Digits(123))
    #print(Digits(400))

    #print(OddElements([0,1,2,3,4,5]))
    #print(OddElements([1,-1,2,-2]))

    #str1='kartiksayee'
    #print(''.join(list(reversed(str1))))

    #str1='this place is fun and so much of fun and loads of fun'
    #lst=str1.split('fun')
    #print(lst)
    #print('NONE'.join(lst))
    #print(str1.replace('fun','NONE'))

    #str1='abcdabxycd'
    #str2='ab'
    #print(str1.count(str2))

    lst=[['A','B','C'],['B','F','D'],['A','D'],['E']]
    #print(EmplDict(lst))
    print(EmplDictSmp(lst))
    lst = [['A'], ['B'], ['D'], ['C'],['E']]
    #print(EmplDict(lst))
    print(EmplDictSmp(lst))


if __name__=='__main__':
    main()