
def WordCount(str1):

    lst={}
    st=0
    end=0
    flg=True
    for i in range(0,len(str1)):
        if str1[i]==' ' or i+1==len(str1):
            if str1[i]==' ':
                end=i
            else:
                end=i+1
            flg=True
            key=str1[st:end]
            if key in lst.keys():
                lst[key]=lst.get(key)+1
            else:
                lst[key]=1
        else:
            if flg==True:
                st=i
                flg=False

    print(lst)

def UniqueDigits(n):

    fnl_lst=[]
    for i in range(10,n+1):

        num=i
        unq_flg=True
        lst={}
        first_time=True
        while(num!=0):
            key=num%10
            if first_time==True:
                lst[key]=1
                first_time=False
            if key in lst.keys() and first_time==False:
                lst[key]=lst.get(key)+1
            else:
                unq_flg=False
            num=int(num/10)

        if unq_flg==True:
            fnl_lst.append(i)

    print(fnl_lst)

def UniqueChar(str1):

    lst={}
    flg=True
    for i in range(0,len(str1)):
        key=str1[i]
        if key in lst.keys():
            flg=False
        else:
            lst[key]=1

    if flg==True:
        print("Unique Character String")
    else:
        print("Non-Unique Character String")

def UnionIntersection(lst1,lst2):

    Int=[]
    Un=[]

    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    for i in range(0,len(big_lst)):
        key=big_lst[i]
        if key in sml_lst and key not in Int:
            Int.append(key)
    print(Int)

    for i in range(0,len(big_lst)):
        key=big_lst[i]

        if key not in Un:
            Un.append(key)

    for i in range(0, len(sml_lst)):
        key = sml_lst[i]

        if key not in Un:
            Un.append(key)
    print(Un)

def SubsetArray(ary1,ary2):

    sml_ary=[]
    big_ary=[]

    if len(ary1)>len(ary2):
        big_ary=ary1
        sml_ary=ary2
    else:
        big_ary=ary2
        sml_ary=ary1

    lst={}
    flg=True
    for i in range(0,len(big_ary)):
        key=big_ary[i]

        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    for i in range(0,len(sml_ary)):
        key=sml_ary[i]

        if key in lst.keys() and lst.get(key)>0:
            lst[key]=lst.get(key)-1
        else:
            flg=False
            break
    if flg==True:
        print("Small ary is a Subset of Big Ary")
    else:
        print("Small ary is NOT a Subset of Big Ary")

def StructureString(str1):

    found=False
    fnl_str=''
    spc_flg=False
    for i in range(0,len(str1)):
        if str1[i]==' ' and found==False:
            continue
        elif str1[i] == ' ' and found == True:
            spc_flg=True
        elif str1[i]!=' ' and spc_flg==True:
            fnl_str=fnl_str+' '+str1[i]
            spc_flg=False
        elif str1[i]!=' ' and spc_flg==False:
            fnl_str=fnl_str+str1[i]
            found=True

    print(fnl_str)

def StringPalindrome(str1):

    st=0
    end=len(str1)-1

    flg=True
    while(st<end):
        if str1[st]!=str1[end]:
            flg=False
            break
        else:
            st=st+1
            end=end-1
    if flg==True:
        print("String is Palindrome")
    else:
        print("String is NOT Palindrome")

def StringExpansion(str1):

    prev_chr=''
    fnl_str=''
    for i in range(0,len(str1)):
        if ord(str1[i])>=48 and ord(str1[i])<=57:
            num=int(str1[i])
            while(num>0):
                fnl_str=fnl_str+prev_chr
                num=num-1
        else:
            prev_chr=str1[i]
    print(fnl_str)

def StringCompression(str1):

    prev_chr=''
    fnl_str=''
    prev_chr=str1[0]
    cnt=1
    for i in range(1,len(str1)):
        if prev_chr!=str1[i]:
            fnl_str=fnl_str+prev_chr+str(cnt)
            cnt=1
        else:
            cnt=cnt+1
        prev_chr=str1[i]

    fnl_str = fnl_str + prev_chr + str(cnt)
    print(fnl_str)

def SingleOccurence(ary):

    fnl_str=[]
    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[:i]:
            fnl_str.append(key)
        else:
            continue
    print(fnl_str)

def SecondMaxElement(ary):

    max=ary[0]
    sec_max=ary[0]
    for i in range(0,len(ary)):
        if ary[i]>max:
            sec_max=max
            max=ary[i]
        elif ary[i]>sec_max:
            sec_max=ary[i]

    print(max)
    print(sec_max)

def ReverseWords(str1):

    fnl_str=''
    st=0
    end=0
    flg=True
    for i in range(0,len(str1)):

        if str1[i]==' ' or i+1==len(str1):
            if str1[i]==' ':
                end=i
            else:
                end=i+1
            key=''.join(reversed(str1[st:end]))
            fnl_str=fnl_str+' '+key
            flg=True
        else:
            if flg==True:
                st=i
                flg=False

    print(fnl_str)

def ReverseString(str1):

    st=0
    end=0
    flg=True
    fnl_str=''

    for i in range(len(str1)-1,-1,-1):
        if str1[i]==' ' or i==0:
            if str1[i]==' ':
                st=i+1
            else:
                st=0
            flg=True
            key=str1[st:end]
            if fnl_str=='':
                fnl_str=fnl_str+key
            else:
                fnl_str=fnl_str+' '+key
            end=st
        else:
            if flg==True:
                end=i+1
                flg=False
    print(fnl_str)

def ReverseNumber(n):

    found=False
    fnl_num=0
    while(n!=0):
        key=n%10
        if key==0 and found==False:
            n = int(n / 10)
            continue
        elif key==0 and found==True:
            fnl_num = fnl_num * 10 + key
        else:
            fnl_num=fnl_num*10+key
            found=True
        n=int(n/10)

    print(fnl_num)

def reverseary(ary1):

    st=0
    end=len(ary1)-1

    while st<end:
        tmp=ary1[st]
        ary1[st]=ary1[end]
        ary1[end]=tmp
        st=st+1
        end=end-1
    print(ary1)

def reverserecur(ary2,st,end):

    if st>=end:
        return
    else:
        tmp=ary2[st]
        ary2[st]=ary2[end]
        ary2[end]=tmp
        reverserecur(ary2,st+1,end-1)

def ReplaceSpaces(str1):

    found=False
    fnl_str=''
    spc_flg=False
    for i in range(0,len(str1)):
        if str1[i]=='$' and found==False:
            continue
        elif str1[i]=='$' and found==True:
            spc_flg=True
            continue
        else:
            if found==False:
                fnl_str=str1[i]
                found=True
            elif spc_flg==False:
                fnl_str=fnl_str+str1[i]

            elif spc_flg==True:
                fnl_str = fnl_str +'%20'+str1[i]
                spc_flg=False

    print(fnl_str)

def RemoveDuplicates(ary):

    fnl_ary=[]

    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[:i]:
            fnl_ary.append(key)
    print(fnl_ary)

def PlusOne(ary,n):

    fnl_num=[]
    carry=0
    for i in range(len(ary)-1,-1,-1):
        if i+1==len(ary):
            val=ary[i]+n
        else:
            val = carry + ary[i]
        fnl_num.append(str(val%10))
        carry=int(val/10)

    if carry!=0:
        fnl_num.append(str(carry))
    fnl_num.reverse()
    print(''.join(fnl_num))

def OddPosition(ary):

    fnl_ary=[]

    for i in range(0,len(ary)):
        if i%2!=0:
            fnl_ary.append(ary[i])
    print(fnl_ary)

def EvenPosition(ary):

    fnl_ary=[]

    for i in range(0,len(ary)):
        if i%2==0:
            fnl_ary.append(ary[i])
    print(fnl_ary)

def NumberPalindrome(num):

    n=num
    fnl_num=0

    while(n!=0):
        fnl_num=fnl_num*10+(n%10)
        n=int(n/10)

    if num==fnl_num:
        print("Palindrome")
    else:
        print("NOT Palindrome")

def MostRecurringElement(ary):

    lst={}

    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    max_key=0
    max_val=0
    for key,val in lst.items():
        if val>max_val:
            max_key=key
            max_val=val

    print(max_key,max_val)

def MinAbsDiff(ary):

    min_abs=9999
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            key=abs(ary[j]-ary[i])
            if key<min_abs:
                min_abs=key
    print(min_abs)

def Median(ary):
    ary.sort()
    if len(ary)%2!=0:
        med=ary[int(len(ary)/2)]
    else:
        med=(ary[int(len(ary)/2)]+ary[int(len(ary)/2)+1])/2
    print(med)

def MaxElement(ary):

    max_ele=0
    for i in range(0,len(ary)):
        if ary[i]>max_ele:
            max_ele=ary[i]

    print(max_ele)

def AddingNumber(num):

    tmp_sum=0
    flg=True
    while flg==True:
        tmp_sum=0
        while num!=0:
            tmp_sum=tmp_sum +(num%10)
            num=int(num/10)
        if tmp_sum>9:
            num=tmp_sum
        else:
            flg=False

    print(tmp_sum)

def AddingTwoNumber(num1,num2):

    if num1>num2:
        big_num=num1
        sml_num=num2
    else:
        big_num=num2
        sml_num=num1

    carry=0
    val=0
    fnl_num=[]
    while big_num!=0:

        if sml_num!=0:
            val=(big_num%10)+(sml_num%10)+carry
            sml_num = int(sml_num / 10)
        else:
            val = (big_num % 10) + carry
        big_num=int(big_num/10)
        fnl_num.append(str(val%10))
        carry=int(val/10)

    if carry!=0:
        fnl_num.append(str(carry))

    fnl_num.reverse()
    print(''.join(fnl_num))

def Fibonaci(n):

    fb=[]
    fb.append(0)
    fb.append(1)

    k=2
    for i in range(3,n):
        fb.append(fb[k-1]+fb[k-2])
        k=k+1
    print(fb)

def cumulativeSum(ary):

    fnl_ary=[]
    sum=0
    for i in range(0,len(ary)):
        sum=sum+ary[i]
        fnl_ary.append(sum)
    print(fnl_ary)

def ReplaceStr(str):

    print(str)
    fnl_str=str.replace('fun','NONE')
    print(fnl_str)
    print(fnl_str.count('NONE'))

def IPaddress(ip):

    print(ip)
    lst=ip.split('.')
    print(lst)

    flg=True
    if len(lst)!=4:
        flg=False
    else:
        for i in range(0,len(lst)):
            try:
                key=int(lst[i])
            except:
                flg=False
                break
            if key>=0 and key<=255:
                continue
            else:
                flg=False
                break
    if flg==True:
        print("Valid IP")
    else:
        print("Invalid IP")

def Percentile(ary,n):

    ary.sort()
    ln=len(ary)-1
    print(ary)
    for i in range(0,len(ary)):
        if (i/ln<n):
            continue
        else:
            break
    print(ary[i])

def UniqueDigits(n):

    lst=[]
    rem=0
    flg=True
    while(n!=0):
        rem=n%10
        if rem in lst:
            flg=False
        else:
            lst.append(rem)
        n=int(n/10)

    if flg==True:
        print("Unique Digits")
    else:
        print("Non-Unique Digits")

import random

def fnl(i):
    return random.random()

def rand(st,end,n):
    return random.randrange(st,end,n)

def Random_sort(ary,n):

    print(random.randint(10,200))
    print(sorted(ary,key=fnl)[:n])
    print(fnl(2))
    print(rand(100,1000,5))

def MovieTimes(tup_list):

    print('Original List:', tup_list)
    print('Sorted List:',sorted(tup_list, key=lambda element: element[0]))
    sort_tup_list = sorted(tup_list, key=lambda element: element[0])

    fnl_tup = []
    fnl_tup.append(tup_list[0])
    k = 0
    i = 1
    while (i < len(sort_tup_list)):
        if sort_tup_list[i][0] < fnl_tup[k][1]:
            if sort_tup_list[i][1] < fnl_tup[k][1]:
                tmp_tup = (fnl_tup[k][0], fnl_tup[k][1])
            else:
                tmp_tup = (fnl_tup[k][0], sort_tup_list[i][1])
            del fnl_tup[k]
            fnl_tup.append(tmp_tup)
        else:
            fnl_tup.append(sort_tup_list[i])
            k = k + 1
        i = i + 1

    print('Final List:', fnl_tup)
    sum = 0
    for i in range(0, len(fnl_tup)):
        sum = sum + (fnl_tup[i][1] - fnl_tup[i][0])
    print(sum)

def CountList(lst):
    out_lst=[]
    for i in lst:
        if isinstance(i,list):
            out_lst.extend(CountList(i))
        else:
            out_lst.append(i)
    return out_lst

def CountTup(lst):
    out_lst=[]
    for i in lst:
        if isinstance(i,(list,tuple)):
            out_lst.extend(CountTup(i))
        else:
            out_lst.append(i)
    return tuple(out_lst)

def NonRecur(ary):

    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[i+1:]:
            print(key)
            break

def ReturnList(n):

    lst=[]

    while n!=0:
        key=n%10
        lst.append(key)
        n=int(n/10)

    lst.reverse()
    print(lst)

def SmlAbsDiff(ary):

    print(ary)
    ary.sort()
    print(ary)

    min=999999

    for i in range(1,len(ary)):
        key=ary[i]-ary[i-1]
        if key<min:
            min=key

    print(min)

def Intersection(ary1,ary2):

    lst=[]

    sml_lst=[]
    big_lst=[]

    if len(ary1)>len(ary2):
        big_lst=ary1
        sml_lst=ary2
    else:
        big_lst = ary2
        sml_lst = ary1

    for i in range(0,len(big_lst)):
        key=big_lst[i]

        if key in sml_lst and key not in lst:
            lst.append(key)

    print(lst)

def MovingZero(ary):

    for i in range(0,len(ary)):
        if ary[i]==0:
            ary.append(0)
            del ary[i]
    print(ary)

def Dissapered(ary):

    min1=min(ary)
    max1=max(ary)

    i=min1
    lst=[]
    while i<=max1:
        if i not in ary:
            lst.append(i)
        i=i+1
    print(lst)

def UniqueCharPos(str):

    lst=list(str)

    for i in range(0,len(lst)):
        key=lst[i]
        if key not in lst[i+1:]:
            print(key,i)
            break

def MinIndex(ary1,ary2):

    min_idx=9999
    val=''

    for i in range(0,len(ary1)):
        key=ary1[i]
        if key in ary2:
            idx=i+ary2.index(key)
            if idx<min_idx:
                min_idx=idx
                val=ary1[i]

    print(val,min_idx)

def CntEleTup(lst):

    cnt=0
    print(lst)
    for i in lst:
        if isinstance(i,tuple):
            break
        else:
            cnt=cnt+1
    print(cnt)

def RepTup(lst,n):

    print(lst)
    out_lst=[]
    for i in lst:
        tmp_tup=tuple(i[:-1]+(n,))
        out_lst.append(tmp_tup)
    print(out_lst)


def GroupingAnagrams(lst):

    dict={}
    print(lst)
    for i in range(0,len(lst)):
        key=lst[i]
        tmp_key=''.join(sorted(key))
        if tmp_key in dict:
            dict[tmp_key].append(key)
        else:
            dict[tmp_key]=[]
            dict[tmp_key].append(key)

    print(dict)

def MergeList(lst1,lst2):
    big_lst=[]
    sml_lst=[]
    fnl_lst=[]

    print(lst1)
    print(lst2)
    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1
    k=0
    i=0
    while(i<len(big_lst)):
        if k<len(sml_lst):
            if big_lst[i]<sml_lst[k]:
                fnl_lst.append(big_lst[i])
                i=i+1
            else:
                fnl_lst.append(sml_lst[k])
                k=k+1
        else:
            fnl_lst.append(big_lst[i])
            i=i+1

    print(fnl_lst)

def GCD(ary):

    ary.sort()
    print(ary)
    sml_num = ary[0]
    big_num = ary[1]
    i=1
    while(i<len(ary)):
        big_num=ary[i]
        while big_num%sml_num!=0:
            rem=big_num%sml_num
            big_num=sml_num
            sml_num=rem
        i=i+1
    print(sml_num)

def main():
    str1 = '       I work          in Amazon in Seattle       I           life         '

    '''  
    lst=str1.split()
    print(lst)
    fnl_str=''
    for i in range(0,len(lst)):
        if fnl_str=='':
            fnl_str=lst[i]
        else:
            fnl_str=fnl_str+' '+lst[i]
    print(fnl_str)
    dict={}
    for i in range(0,len(lst)):
        key=lst[i]
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1
    print(dict)
    '''

    #WordCount(str1)


    #n=1000
    '''
    lst={}
    flg=True
    while(n!=0):
        rem=n%10
        if rem in lst.keys():
            flg=False
            break
        else:
            lst[rem]=1
        n=int(n/10)
    print(flg)
    '''
    #UniqueDigits(n)

    #str1='marya'
    #UniqueChar(str1)

    #lst1 = [1, 3, 4,3, 5, 7,5]
    #lst2 = [2, 3, 5, 6,5]
    #UnionIntersection(lst1,lst2)

    #ary1 = [11, 1, 13, 21, 3, 7]
    #ary2 = [11, 3, 7, 1, 1]

    #SubsetArray(ary1, ary2)

    #ary1 = [1, 2, 3, 4, 5, 6]
    #ary2 = [1, 2, 4]

    #SubsetArray(ary1, ary2)

    #ary1 = [10, 5, 2, 23, 19]
    #ary2 = [19, 5, 3]

    #SubsetArray(ary1, ary2)

    #str1 = '    The     sky is     very blue     '
    '''
    fnl_str=''
    found=False
    spc_flg=False

    for i in range(0,len(str1)):
        if str1[i]==' ' and found==False:
            continue
        elif str1[i] == ' ' and found == True:
            spc_flg=True
        else:
            if found==False:
                fnl_str=str1[i]
                found=True
            else:
                if spc_flg==True:
                    fnl_str=fnl_str+' '+ str1[i]
                else:
                    fnl_str=fnl_str+str1[i]
            spc_flg=False

    print(fnl_str,len(fnl_str))
    '''
    #StructureString(str1)

    #str1 = 'malayalam'
    #StringPalindrome(str1)

    #str1 = 'a3b1c5a2'
    '''
    fnl_str=''
    prev_char=str1[0]
    for i in range(1,len(str1)):
        if ord(str1[i])>=48 and ord(str1[i])<=57:
            num=int(str1[i])
            while(num>0):
                fnl_str=fnl_str+prev_char
                num=num-1
        prev_char=str1[i]

    print(fnl_str)
    '''
    #StringExpansion(str1)

    #str1 = 'aabcccccaa'
    '''
    fnl_str=''
    prev_char=str1[0]
    cnt=1
    for i in range(1,len(str1)):
        if prev_char!=str1[i]:
            fnl_str=fnl_str+prev_char+str(cnt)
            cnt=1
        else:
            cnt=cnt+1
        prev_char=str1[i]

    fnl_str=fnl_str+prev_char+str(cnt)
    print(fnl_str)
    '''

    #StringCompression(str1)

    #ary = [1, 2, 2,2,3,4,56,3,3,3, 7, 9, 4, 9, 4, 85, 6, 34, 6, 1, 10, 34, 45]
    '''
    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[i+1:] and key not in ary[:i]:
            fnl_lst.append(key)
        else:
            continue
    print(fnl_lst)
    '''
    #SingleOccurence(ary)

    #ary = [5, 89, 20, 64, 20, 45, 53]
    '''
    max=ary[0]
    sec_max=ary[0]

    for i in range(0,len(ary)):
        if ary[i]>max:
            sec_max=max
            max=ary[i]
        elif ary[i]>sec_max:
            sec_max=ary[i]
    print(sec_max)
    '''

    #SecondMaxElement(ary)

    #str1 = 'The Sky is Blue'
    '''
    lst=str1.split()
    print(lst)
    fnl_str=''

    for i in range(0,len(lst)):
        key=(''.join(reversed(lst[i])))
        if fnl_str=='':
            fnl_str=key
        else:
            fnl_str=fnl_str+' '+key
    print(fnl_str)
    '''
    #ReverseWords(str1)

    #str1 = 'I am using hackerrank to improve programming'
    '''
    lst=str1.split()
    print(lst)
    fnl_str=''
    for i in range(len(lst)-1,-1,-1):
        if fnl_str=='':
            fnl_str=lst[i]
        else:
            fnl_str=fnl_str+' '+lst[i]
    print(fnl_str)
    '''
    #ReverseString(str1)

    #n = 345
    '''
    lst=[]
    found=False
    while(n!=0):
        tmp=n%10
        if tmp==0 and found==False:
            n = int(n / 10)
            continue
        elif tmp!=0:
            found=True
            lst.append(str(tmp))
        elif tmp==0 and found==True:
            lst.append(str(tmp))
        n=int(n/10)
    print(''.join((lst)))
    '''

    #ReverseNumber(n)

    #n = 3405000
    #ReverseNumber(n)

    #ary1 = [1, 2, 3, 4, 5, 6, 7]
    #print(ary1)
    #reverseary(ary1)

    #ary2 = [11, 22, 33, 44, 55, 66, 77]
    #print(ary2)
    #reverserecur(ary2, 0, len(ary2) - 1)
    #print(ary2)

    #str1 = '$$$$$Mr$$John$Smith$$$$$$'
    #str2 = 'Mr$$John$Smith'
    #str3 = '$$$$$Mr$$John$Smith'
    #str4 = '$$$$$Mr$$John$$$$Smith$'

    '''
    fnl_str=''
    found=False
    spc_flg=False
    for i in range(0,len(str1)):
        key=str1[i]
        if key=='$' and found==False:
            continue
        elif key=='$' and found==True:
            spc_flg=True
        elif key!='$':
            if found==False:
                fnl_str=fnl_str+key
                found=True
            elif spc_flg==True:
                fnl_str=fnl_str+'%20'+key
                spc_flg=False
            else:
                fnl_str=fnl_str+key
    print(fnl_str)
    '''
    #ReplaceSpaces(str1)
    #ReplaceSpaces(str2)
    #ReplaceSpaces(str3)
    #ReplaceSpaces(str4)

    #ary = [1, 1, 1, 2, 2, 3, 5, 5, 7, 7, 7, 8, 9, 10, 34, 34, 56, 56, 56]
    '''
    lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
        if key not in lst:
            lst.append(key)
    print(lst)
    '''
    #RemoveDuplicates(ary)

    #ary = [9, 9, 9, 7]
    #n = 9
    #PlusOne(ary, n)

    #ary = [0, 1, 2, 3, 4, 5]
    '''
    lst=[]
    for i in range(0,len(ary)):
        if i%2!=0:
            lst.append(ary[i])
    print(lst)
    '''
    #OddPosition(ary)

    #ary = [1, -1, 2, -2,5,8,9]
    '''
    lst=[]
    for i in range(0,len(ary)):
        if i%2==0:
            lst.append(ary[i])
    print(lst)
    '''
    #EvenPosition(ary)

    #num = 112211
    '''
    tmp=num
    fnl_num=0
    while(tmp!=0):
        rem=tmp%10
        fnl_num=fnl_num*10+rem
        tmp=int(tmp/10)
    print(num,fnl_num)
    if fnl_num==num:
        print(True)
    else:
        print(False)
    '''
    #NumberPalindrome(num)

    #num = 3344882
    #NumberPalindrome(num)

    #ary = [4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1]
    ''''
    lst={}
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1
    print(lst)
    max_val=0
    max_key=0
    for key,val in lst.items():
        if val>max_val:
            max_val=val
            max_key=key
    print(max_key,max_val)
    '''
    #MostRecurringElement(ary)

    #ary = [30, 5, 20, 9]
    '''
    ary.sort()
    print(ary)
    min=9999
    for i in range(1,len(ary)):
        key=abs(ary[i]-ary[i-1])
        
        if key<min:
            min=key
    print(min)
    '''
    #MinAbsDiff(ary)

    #ary1 = [5, 89, 20, 64, 20, 45]

    #Median(ary1)

    #ary1 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]

    #Median(ary2)
    '''
    ary1.sort()
    print(ary1)
    if len(ary1)%2!=0:
        med=ary1[int(len(ary1)/2)]
    else:
        med=(ary1[int((len(ary1)-1)/2)]+ary1[(int((len(ary1)-1)/2))+1])/2
    print(med)
    '''

    #ary = [5, 89, 20, 64, 20, 45, 53]

    #MaxElement(ary)

    #num = 38
    '''
    sum=0
    tmp=num
    while(tmp>9):
        sum=0
        while(tmp!=0):
            sum=sum+tmp%10
            tmp=int(tmp/10)
        tmp=sum
    print(sum)
    '''
    #AddingNumber(num)

    #num = 679
    #AddingNumber(num)

    #num1 = 38
    #num2 = 679
    '''
    if num1>num2:
        big_num=num1
        sml_num=num2
    else:
        big_num=num2
        sml_num=num1

    val=0
    carry=0
    lst=[]
    while big_num!=0:

        if sml_num!=0:
            val=big_num%10+sml_num%10+carry
            sml_num=int(sml_num/10)
        else:
            val = big_num % 10 + carry
        big_num=int(big_num/10)
        lst.append(str(val%10))
        carry=int(val/10)

    print(lst)
    if carry>0:
        lst.append(str(carry))
    print(''.join(reversed(lst)))
    '''
    #AddingTwoNumber(num1,num2)

    #n=100
    '''
    fib=[]
    fib.append(0)
    fib.append(1)
    cnt=2
    i=1
    while(cnt<n):
        key=fib[i]+fib[i-1]
        fib.append(key)
        i=i+1
        cnt=cnt+1
    print(fib)
    '''
    #Fibonaci(n)

    #ary = [1, 1, 1]
    #cumulativeSum(ary)

    #ary = [1, -1, 3]
    '''
    sum = 0
    lst = []
    for i in range(0, len(ary)):
        sum = sum + ary[i]
        lst.append(sum)
    print(lst)
    '''
    #cumulativeSum(ary)

    str = "Amazon is a fun place to fun work and is very fun to be"
    '''
    lst=str.split()
    print(lst)
    fnl_str=''
    for i in range(0,len(lst)):
        key=lst[i]
        if fnl_str=='':
            if key.lower()=='fun':
                fnl_str='NONE'
            else:
                fnl_str=key
        else:
            if key.lower()=='fun':
                fnl_str = fnl_str + ' ' + 'NONE'
            else:
                fnl_str=fnl_str+' '+key
    print(fnl_str)
    '''
    #ReplaceStr(str)

    #ip='69.89.18.226'
    #IPaddress(ip)

    #ip='69.89.345.226'
    #IPaddress(ip)

    #ip = '69.89.345'
    #IPaddress(ip)

    #ip = '69.89.345.aa'
    #IPaddress(ip)

    '''
    lst=ip.split('.')
    flg=True
    if len(lst)!=4:
        flg=False
    else:
        for i in range(0,len(lst)):
            try:
                key=int(lst[i])
            except:
                flg=False
                break
            if key>=0 and key<=255:
                continue
            else:
                flg=False
    print(flg)
    '''
    ary = [5, 89, 20, 64, 20, 45]
    n = 0.75

    #Percentile(ary, n)

    #ary = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    #n = 0.9
    #Percentile(ary, n)
    '''
    ary.sort()
    print(ary)

    k = len(ary)-1
    for i in range(0, len(ary)):
        if i / k < 0.75:
            continue
        else:
            break
    print(ary[i])
    '''
    #n=4592
    #UniqueDigits(n)

    #n=1998
    #UniqueDigits(n)
    '''
    lst={}
    flg=True
    while(n!=0):
        key=n%10
        if key in lst.keys():
            flg=False
        else:
            lst[key]=1
        n=int(n/10)
    print(flg)
    '''
    #ary=[1,2,3,4,5,6,7,8,9]
    #n=5
    '''
    import random

    def fnl(i):
        return random.random()

    print(sorted(ary,key=fnl)[:n])
    '''
    #Random_sort(ary,n)

    #str='aabbccabab'
    #sub_str='ab'
    #print(str.count(sub_str))

    #print(str.count(sub_str))

    tup_list=[(0,15),(20,25),(40,50),(10,30),(45,54),(55,65)]
    #MovieTimes(tup_list)

    '''
    sort_list=sorted(tup_list, key=lambda x:x[0])
    print(tup_list)
    print(sort_list)

    fnl_tup=[]
    fnl_tup.append(sort_list[0])
    k=0
    for i in range(1,len(sort_list)):
        if sort_list[i][0]<fnl_tup[k][1]:
            if sort_list[i][1]<fnl_tup[k][1]:
                continue
            else:
                tmp_tup=(fnl_tup[k][0],sort_list[i][1])
                del fnl_tup[k]
                fnl_tup.append(tmp_tup)
        else:
            fnl_tup.append(sort_list[i])
            k=k+1
    print(fnl_tup)

    sum=0
    for i in range(0,len(fnl_tup)):
        sum=sum+(fnl_tup[i][1]-fnl_tup[i][0])
    print(sum)
    '''

    '''
    def fnl(ary):
        return ary[-1]
    ary=['xy','bc','ur','aa','il']
    print(ary)
    print(sorted(ary,key=fnl))
    print(sorted(ary, key=str.lower))
    '''

    #tup=(5,4,3)
    #print(len(tup))

    '''
    str = 'but soft what light in yonder window breaks'
    lst=str.split(' ')
    print(lst)
    print(sorted(lst,key=len))
    '''

    '''
    d = {'z': 10, 'b': 1, 'c': 22}
    lst=[]
    for key,val in d.items():
        lst.append((key,val))
    print(lst)
    print(sorted(lst,key=lambda element:element[1] ))
    #print(lst)
    '''

    #lst=[1,2,[1,2,3,[3,3],(5,6,7)],4,5,6,[7,6,4],[8,7,4,5,[6,7,8]]]
    '''
    print(lst)
    def kartik(lst):
        out_lst=[]
        for i in lst:
            if isinstance(i,(list,tuple)):
                out_lst.extend(kartik(i))
            else:
                out_lst.append(i)
        return out_lst

    print(kartik(lst))
    '''
    #print(CountList(lst))
    #tup = (1, 2, (1, 2, 3, (3, 3), [5, 6, 7]), 4, 5, 6, (7, 6, 4), (8, 7, 4, 5, (6, 7, 8)))
    #print(tup)
    #print(CountTup(tup))


    #tup=(1,2,3)
    #print(tup)
    #tup=tup+(5,6)
    #print(tup)

    #lst = [1, 5, 3, 1, 2, 5, 6, 7, 8]
    #lst.remove(5)
    #print(lst)

    '''
    str='this is kartik sayee'
    if 'kartika' in str:
        print(True)
    '''

    #ary=[1,3,4,9,6,3,1,2,4,5,6,3,8]
    #NonRecur(ary)

    #n=123
    #ReturnList(n)

    #n = 4000
    #ReturnList(n)

    '''
    ary=[30,15,21,17,24,5]
    SmlAbsDiff(ary)

    ary = [1, -2, 3, -4, 4, -5]
    SmlAbsDiff(ary)

    ary = [1,2,3,4,4,5]
    SmlAbsDiff(ary)
    '''

    #ary1=[1, 2, 2, 1]
    #ary2=[2, 2]

    #Intersection(ary1,ary2)

    #ary=[0, 1, 0, 3, 12]
    '''
    n=len(ary)
    i=0
    while(i<n):
        if ary[i]==0:
            n=n-1
            del ary[i]
            i=i-1
        else:
            i=i+1
    print(ary)
    '''
    #MovingZero(ary)

    #ary=[4,3,2,7,8,2,3,1]
    #Dissapered(ary)

    #str='leetcode'
    #lst=list(str)
    #print(lst)
    #UniqueCharPos(str)

    #str = 'loveleetcode'
    #UniqueCharPos(str)

    #ary1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
    #ary2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    #MinIndex(ary1,ary2)

    #ary1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    #ary2 = ["KFC", "Shogun", "Burger King"]
    #MinIndex(ary1, ary2)

    #lst=[1,2,3,4]
    #lst.insert(1,5)
    #print(lst)

    #price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    #print(sorted(price,key=lambda x:x[1],reverse=True))

    #lst = [10, 20, 30, (10, 20), 40]
    #CntEleTup(lst)

    #lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    '''
    n=100
    fnl_lst=[]
    for i in range(0,len(lst)):
        tmp_tup=tuple(lst[i][:-1])+(100,)
        fnl_lst.append(tmp_tup)
    print(fnl_lst)
    '''
    #RepTup(lst,n)

    #lst=['1','2','3']
    #print(lst)
    #print(''.join(lst))

    #tup=('a','b','c')
    #print(tup)
    #print(''.join(tup))

    #lst=["eat", "tea", "tan", "ate", "nat", "bat"]
    #GroupingAnagrams(lst)
    '''
    str='ab'
    if len(str)>=3 and str[-3:]!='ing':
        print(str+'ing')
    elif len(str) >= 3 and str[-3:] == 'ing':
        print(str+'ly')
    else:
        print(str)
    '''

    #lst=['aggarwal','zaveri','ab','prashant','kot','ajit','kartik']

    #print(len(sorted(lst,key=len)[-1]))

    #str='kartikey'
    #fnl_str=str[-1]+str[1:len(str)-1]+str[0]
    #print(fnl_str)

    '''
    str='sanfrancisco'
    fnl_str=''
    for i in range(0,len(str)):
        if i%2==0:
            continue
        else:
            fnl_str=fnl_str+str[i]
    print(fnl_str)
    '''

    #lst=['red', 'white', 'black', 'red', 'green', 'black']
    #print(lst)
    #print(set(lst))
    #print(sorted(set(lst)))


    #lst=['abc', 'xyz', 'aba', '1221']

    '''
    tmp_str=''
    cnt=0
    for i in range(0,len(lst)):
        tmp_str=lst[i]
        if tmp_str[0]==tmp_str[-1]:
            cnt=cnt+1

    print(cnt)
    '''

    #lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    #print(sorted(lst,key=lambda x:x[1]))

    #lst=['a','b','c','d']
    #print(''.join(lst))

    #lst1=[10, 20, 30]
    #lst2=[40, 50, 60]
    #lst1.extend(lst2)
    #print(lst1)

    #lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    #print(max(lst,key=sum))

    #lst=[(4, 1), (1, 2), (6, 0)]
    #print(min(lst,key=lambda x:x[-1]))

    '''
    lst1=[1, 3, 5, 7, 9, 10]
    lst2=[2, 4, 6, 8]
    fnl_lst=lst1[:-1]
    fnl_lst.extend(lst2)
    print(fnl_lst)
    '''
    '''
    lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    n=5
    fnl_lst=[]
    cnt=1
    tmp_lst=[]
    for i in range(0,len(lst)):
        if cnt<=5:
            tmp_lst.append(lst[i])
        else:
            fnl_lst.append(tmp_lst)
            cnt=1
            tmp_lst=[]
            tmp_lst.append(lst[i])
        cnt=cnt+1
    fnl_lst.append(tmp_lst)
    print(fnl_lst)
    '''

    #import random
    #lst=['Red', 'Blue', 'Green', 'White', 'Black']
    #print(random.choice(lst))

    #lst1=[3, 4, 6, 10, 11, 18]
    #lst2=[1, 5, 7, 12, 13, 19, 21]
    #print(lst1)
    #print(lst2)

    #lst1.extend(lst2)

    #print(sorted(lst1))
    #lst1 = [3, 4, 6, 10, 11, 18]
    #lst2 = [1, 5, 7, 12, 13, 19, 21]
    '''
    print(lst1)
    print(lst2)

    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    i=0
    j=0
    fnl_lst=[]
    while i<len(big_lst):
        if j<len(sml_lst):
            if big_lst[i]<sml_lst[j]:
                fnl_lst.append(big_lst[i])
                i=i+1
            else:
                fnl_lst.append(sml_lst[j])
                j=j+1
        else:
            fnl_lst.append(big_lst[i])
            i=i+1
    print(fnl_lst)
    '''
    #MergeList(lst1,lst2)

    #ary = [54, 108, 144]
    '''
    ary.sort()
    sml_num=ary[0]
    big_num=ary[1]

    i=1

    while(i<len(ary)):
        big_num=ary[i]
        while(big_num%sml_num!=0):
            rem=big_num%sml_num
            big_num=sml_num
            sml_num=rem
        i=i+1
    print(sml_num)
    '''
    #GCD(ary)

    #str='i am doing work cause i work study work doing seattle city city'
    #lst=str.split(' ')
    #print(lst)
    #unq=set(lst)
    #print(unq)
    #print(len(unq))

    '''
    str1='ab'
    str2='bacabdacabfacab'
    if str1 in str2:
        print(True)
    else:
        print(False)
    print(str2.count(str1))
    '''
    '''
    lst=[10,20,30,(10,20),40]
    cnt=0
    for i in lst:
        if isinstance(i,tuple):
            break
        else:
            cnt=cnt+1
    print(cnt)
    '''

    #lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    #print(max(lst,key=sum))

    str1='  i am   kartik   sayee   '
    '''
    print(str1)
    lst=str1.split()
    print(lst)
    fnl_str=''
    for i in range(0,len(lst)):
        if fnl_str=='':
            fnl_str=lst[i]
        else:
            fnl_str=fnl_str+' '+lst[i]
    print(fnl_str,len(fnl_str))

    fnl_str=''
    spc_flg=False
    found=False
    for i in range(0,len(str1)):
        if str1[i]==' ' and found==False:
            continue
        elif str1[i]==' ' and found==True:
            spc_flg=True
        else:
            found=True
            if fnl_str=='':
                fnl_str=str1[i]
            elif spc_flg==True:
                fnl_str=fnl_str+' '+str1[i]
                spc_flg=False
            else:
                fnl_str = fnl_str + str1[i]
    print(fnl_str, len(fnl_str))
    '''
    '''
    line = '  Here      we     go     '
    lst=line.split()
    print(lst)
    print(line)
    print(line.strip())
    '''

    '''
    dict={'k':2,'y':3}
    print(dict.items())

    for key,val in dict.items():
        print(key,val)
    '''

    #lst=[34, 1, 0, -23]
    #print(list(filter(lambda x:x>0,lst)))

    '''
    lst=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
    print(lst)
    fnl_lst=[]
    for i in lst:
        fnl_lst.extend(i)
    print(fnl_lst)
    print(set(fnl_lst))
    '''
    '''
    lst=[1, 2, -8, -2, 0]

    min=lst[0]
    sec_min=lst[0]

    for i in range(1,len(lst)):
        if lst[i]<min:
            sec_min=min
            min=lst[i]
        elif lst[i]<sec_min:
            sec_min=lst[i]
    print(sec_min)
    '''
    '''
    str="The quick brown fox jumps over the lazy dog"
    lst=str.split()
    print(lst)
    fnl_lst=[]
    for i in range(0,len(lst)):
        if len(lst[i])>3:
            fnl_lst.append(lst[i])
    print(fnl_lst)
    '''
    '''
    lst = [1, 2, -8, -2, 0]
    print(min(sorted(lst)))
    '''
    '''
    lst=set([1,2,3,1,2,3,4,5])
    print(lst)
    for i in lst:
        print(i)
    lst.pop()
    print(lst)
    lst.add('a')
    print(lst)
    lst.discard('a')
    print(lst)
    '''
    '''
    tup=(2, 4, 5, 6,5, 2, 3, 4, 4, 7 )
    print(tup)
    lst=[]
    for i in range(0,len(tup)):
        key=tup[i]
        if key in tup[i+1:] or key in tup[:i]:
            lst.append(key)
    print(lst)
    '''
    '''
    tup=(5, 10, 15, 20)
    print(tup)
    lst=reversed(tup)
    print(list(lst))
    '''

    '''
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    print(d1)
    print(d2)
    fnl_dict={}

    for key,val in d1.items():
        fnl_dict[key]=val
    for key,val in d2.items():
        if key in fnl_dict.keys():
            fnl_dict[key]=fnl_dict.get(key)+val
        else:
            fnl_dict[key]=val
    print(fnl_dict)
    '''
    '''
    lst=[{"V": "S001"}, {"V": "S002","V4": "S024"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    print(lst)
    fnl_lst=[]
    for i in range(0,len(lst)):
        for key,val in lst[i].items():
            fnl_lst.append(val)
    print(fnl_lst)
    print(list(set(fnl_lst)))
    '''
    '''
    dict={'Math':81, 'Physics':83, 'Chemistry':87}

    fnl_lst=[]
    for key,val in dict.items():
        tmp_tup=(key,val)
        fnl_lst.append(tmp_tup)
    print(fnl_lst)
    print(sorted(fnl_lst,key=lambda x:x[1],reverse=True))
    '''
    '''
    str='   this    is only is     kartik work          only this            work  '
    lst=str.split()
    print(lst)
    print(set(lst))
    print(len(set(lst)))
    '''

    #lst=[4,5,23,2,5,6,78,9,1,100,100,99]
    #print(max(lst))
    '''
    #ary=[1,2,2,1]
    #ary = [1, 1]
    #ary = [1, 2, 2, 1,13]
    ary = [1, 2, 2, 1,13,4,5]
    sum=0
    flg=False
    for i in range(0,len(ary)):
        if ary[i]==13:
            flg=True
            continue
        elif flg==True:
            flg=False
            continue
        else:
            sum=sum+ary[i]
    print(sum)
    '''
    '''
    #ary=[1,2,2]
    ary = [1, 2, 2,6,99,99,7]
    #ary = [1, 1, 6,7,2]

    flg=False
    sum=0
    for i in range(0,len(ary)):
        if ary[i]==6:
            flg=True
            continue
        elif ary[i]==7 and flg==True:
            flg=False
            continue
        elif flg==False:
            sum=sum+ary[i]
    print(sum)
    '''
    '''
    str='hello world! 123'

    num_cnt=0
    let_cnt=0

    for i in range(0,len(str)):
        if (str[i]>='A' and str[i]<='Z') or (str[i]>='a' and str[i]<='z'):
            let_cnt=let_cnt+1
        elif (str[i]>='0' and str[i]<='9'):
            num_cnt=num_cnt+1
    print(let_cnt,num_cnt)
    '''
    '''
    str='a+aa+aaa+aaaa'
    cnt=0
    for i in range(0,len(str)):
        cnt=cnt+ord(str[i])
    print(cnt)
    '''
    '''
    str='1,2,3,4,5,6,7,8,9'
    lst=str.split(',')
    fnl_lst=[]
    print(lst)

    for i in range(0,len(lst)):
        if i%2==0:
            fnl_lst.append(lst[i])
    print(fnl_lst)
    '''
    '''
    sml_flg=False
    cap_flg=False
    num_flg=False
    spc_flg=False

    str='ABd1234@1'
    '''

    str1='abhi'
    str2='hibb'

    #if ''.join(sorted(str1))==''.join(sorted(str2)):
    #    print(True)
    #else:
     #   print(False)

    import collections


if __name__=='__main__':
    main()
