import collections

def Anagram(str1,str2):

    if len(str1)!=len(str2):
        return False
    else:
        if ''.join(sorted(str1))==''.join(sorted(str2)):
            return True
        else:
            return False

def StructureString(str):

    lst=str.split()
    return ' '.join(lst)

def UniqueNumber(n):

    lst={}
    flg=True

    while n!=0:
        key=n%10
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        elif key not in lst.keys() and flg==True:
            lst[key]=1
            flg=False
        elif flg==False:
            return False
        n=int(n/10)
    return True

def UniqueChar(str1):

    if len(str1)==len(set(list(str1))):
        return True
    else:
        return False

def Union(lst1,lst2):

    return set(lst1).union(set(lst2))

def UnionP(lst1,lst2):

    lst=[]

    for l in lst1:
        if l not in lst:
            lst.append(l)
    for l in lst2:
        if l not in lst:
            lst.append(l)
    return lst

def Intersection(lst1,lst2):

    return set(lst1).intersection(set(lst2))

def IntersectionP(lst1,lst2):

    lst=[]

    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    for l in big_lst:
        if l in sml_lst and l not in lst:
            lst.append(l)

    return lst

def SubsetArray(lst1,lst2):

    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    lst={}

    for l in big_lst:
        if l in lst.keys():
            lst[l]=lst.get(l)+1
        else:
            lst[l]=1

    for l in sml_lst:
        if l in lst.keys() and lst.get(l)>0:
            lst[l]=lst.get(l)-1
        else:
            return False

    return True

def StringPalindrome(str1):

    st=0
    end=len(str1)-1

    while st<end:
        if str1[st]!=str1[end]:
            return False

        st=st+1
        end=end-1

    return True

def StringExpansion(str1):

    lst=[]

    prev_chr=str1[0]
    for i in range(1,len(str1)):

        if ord(str1[i])>=48 and ord(str1[i])<=57:
            n=int(str1[i])
            cnt=0
            while cnt<n:
                lst.append(prev_chr)
                cnt=cnt+1
        else:
            prev_chr=str1[i]

    return ''.join(lst)

def StringCompression(str1):

    lst=[]

    prev_chr=str1[0]
    cnt=1
    for i in range(1,len(str1)):

        if prev_chr==str1[i]:
            cnt=cnt+1
        else:
            lst.append(prev_chr)
            lst.append(str(cnt))
            cnt=1
        prev_chr=str1[i]

    lst.append(prev_chr)
    lst.append(str(cnt))
    return ''.join(lst)

def SingleOccurence(ary):

    lst=[]

    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[i+1:] and key not in ary[:i]:
            lst.append(key)

    return lst

def SecondMax(ary):

    return sorted(list(set(ary)),reverse=True)[1]

def ReverseWords(ary):

    lst=ary.split()
    fnl_lst=[]

    for l in lst:
        key=''.join(reversed(l))
        fnl_lst.append(key)

    return ' '.join(fnl_lst)

def ReverseNumber(n):

    lst=[]

    flg=False

    while n!=0:
        rem=n%10
        if rem==0 and flg==False:
            n=int(n/10)
            continue
        else:
            flg=True
            lst.append(str(rem))
            n=int(n/10)

    return ''.join(lst)

def ReverseAry(ary):

    st=0
    end=len(ary)-1

    while st<end:
        tmp=ary[st]
        ary[st]=ary[end]
        ary[end]=tmp
        st=st+1
        end=end-1

    return ary

def ReplaceString(str):

    lst=str.split('$')
    fnl_lst=[]

    for l in lst:
        if l=='':
            continue
        else:
            fnl_lst.append(l)
    return ' '.join(fnl_lst)

def RemoveDuplicates(ary):

    lst=[]

    for l in ary:
        if l not in lst:
            lst.append(l)
    return lst

def PlusOne(ary,n):
    carry=0
    lst=[]
    for i in range(len(ary)-1,-1,-1):
        val=ary[i]+carry+n
        carry=int(val/10)
        rem=val%10
        lst.append(str(rem))
        n=0
    if carry>0:
        lst.append(str(carry))
    return ''.join(reversed(lst))

def OddPosition(ary):

    lst=[]
    for i in range(0,len(ary)):
        if i%2!=0:
            lst.append(ary[i])
    return lst


def EvenPosition(ary):
    lst = []
    for i in range(0, len(ary)):
        if i % 2 == 0:
            lst.append(ary[i])
    return lst

def NumberPalindrome(n):

    lst=[]

    tmp=n
    fnl_num=0

    while tmp!=0:
        rem=tmp%10
        fnl_num=fnl_num*10+rem
        tmp=int(tmp/10)

    if fnl_num==n:
        return True
    else:
        return False

def Add2List(lst1,lst2):

    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    j=len(sml_lst)-1
    carry=0
    fnl_lst=[]
    for i in range(len(big_lst)-1,-1,-1):

        if j>=0:
            val=big_lst[i]+sml_lst[j]+carry
            j=j-1
        else:
            val=big_lst[i]+carry

        carry=int(val/10)
        rem=val%10
        fnl_lst.append(str(rem))

    if carry>0:
        fnl_lst.append(str(carry))
    return ''.join(reversed(fnl_lst))

def IPvalidate(ip):

    lst=ip.split('.')

    for l in lst:
        try:
            if int(l)>=0 and int(l)<=255:
                continue
            else:
                return False
        except:
            return False
    return True

def FriendsList(lst):

    dict={}

    for l in lst:
        for key in l:
            if key in dict.keys():
                dict[key]=dict.get(key)+len(l)-1
            else:
                dict[key]=len(l)-1
    return dict

def ReplaceFun(str1):

    print(str1)
    lst=str1.split('fun')
    return 'NONE'.join(lst)

def GCD(lst):

    lst.sort()

    sml_num=lst[0]

    for i in range(1,len(lst)):
        big_num=lst[i]
        while big_num%sml_num!=0:
            rem=big_num%sml_num
            big_num=sml_num
            sml_num=rem

    return sml_num

def DoGCD(big_num,sml_num):

    while big_num%sml_num!=0:
        rem=big_num%sml_num
        big_num=sml_num
        sml_num=rem

    return sml_num

def LCM(lst):

    lst.sort()

    sml_num=lst[0]

    for i in range(1,len(lst)):
        big_num=lst[i]
        gcd=DoGCD(big_num,sml_num)
        lcm=big_num*sml_num/gcd
        sml_num=lcm
    return int(lcm)

def MergeList(lst1,lst2):

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
    return fnl_lst

def MovieTimes(tup_list):

    print(tup_list)

    sort_list=sorted(tup_list,key=lambda x:x[0])
    print(sort_list)

    fnl_lst=[]
    fnl_lst.append(sort_list[0])
    j=0
    i=1
    while i<len(sort_list):

        if fnl_lst[j][1]>sort_list[i][0] and fnl_lst[j][1]<sort_list[i][1]:
            tmp_tup=(fnl_lst[j][0],sort_list[i][1])
            del fnl_lst[j]
            fnl_lst.append(tmp_tup)
        elif fnl_lst[j][1]<sort_list[i][0]:
            j=j+1
            fnl_lst.append(sort_list[i])

        i=i+1
    sum=0
    print(fnl_lst)
    for k in range(0,len(fnl_lst)):
        sum=sum+(fnl_lst[k][1]-fnl_lst[k][0])

    return sum

def main():

    #str1='MARY'
    #str2='ARMY'
    #print(Anagram(str1,str2))

    #str= '       I work          in Amazon in Seattle       I           life         '
    #print(StructureString(str))

    #n=1000
    #print(UniqueNumber(n))

    #str1='mary'
    #print(UniqueChar(str1))

    #lst1 = [1, 3, 4,3, 5, 7,5]
    #lst2 = [2, 3, 5, 6,5]
    #print(Union(lst1,lst2))
    #print(UnionP(lst1, lst2))
    #print(Intersection(lst1, lst2))
    #print(IntersectionP(lst1, lst2))

    #ary1 = [11, 1, 13, 21, 3, 7,1]
    #ary2 = [11,3, 7, 1,1]
    #print(SubsetArray(ary1, ary2))

    #str1 = 'malayalam'
    #print(StringPalindrome(str1))

    #str1 = 'a3b1c5a2'
    #print(StringExpansion(str1))

    #str1 = 'aabcccccaa'
    #print(StringCompression(str1))

    #ary = [1, 2, 2, 2, 3, 4, 56, 3, 3, 3, 7, 9, 4, 9, 4, 85, 6, 34, 6, 1, 10, 34, 45]
    #print(SingleOccurence(ary))

    #ary = [5, 89,89,89, 20, 64, 20, 45,64,64,64, 53]
    #print(SecondMax(ary))

    #str1 = 'I am using hackerrank to improve programming'
    #print(ReverseWords(str1))

    #n= 340500
    #print(ReverseNumber(n))

    #ary = [1, 2, 3, 4, 5, 6, 7]
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

    #ary1=[9,9,8,7]
    #ary2=[6,4,5]
    #print(Add2List(ary1,ary2))

    #ary = [4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1]
    #lst=collections.Counter(ary).most_common()
    #print(lst)
    #print(list(filter(lambda x:x[1]>1,lst)))
    '''
    lst = [(1, 2), (3, 4),7, (8, 9)]
    fnl_lst=[]
    for l in lst:
        if isinstance(l,(list,tuple)):
            fnl_lst.extend(l)
        else:
            fnl_lst.append(l)
    print(fnl_lst)
    '''

    #color_dict = {'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
    #print(sorted(color_dict.items(),key=lambda x:x[0], reverse=True))

    #str1 = 'w3resource'
    #print(collections.Counter(str1).most_common())

    #dict=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
    #print(sorted(dict,key=lambda x:x['key']['subkey'], reverse=True))

    #ip = '69.89.18.226'
    #print(IPvalidate(ip))

    #ip = '69.89.345.226'
    #print(IPvalidate(ip))

    #ip = '69.89.345'
    #print(IPvalidate(ip))

    #ip = '69.89.345.aa'
    #print(IPvalidate(ip))

    #lst = [['A', 'B', 'C'], ['B', 'F', 'D'], ['A', 'D'], ['E']]
    #print(FriendsList(lst))
    #lst = [['A'], ['B'], ['D'], ['C'],['E']]
    #print(FriendsList(lst))

    #str1='this place is fun and so much of fun and loads of fun'
    #print(ReplaceFun(str1))

    #print(GCD([12,18,30]))
    #print(GCD([12,21,30]))
    #print(GCD([23,17,89]))

    #print(LCM([12,24,36]))
    #print(LCM([2,3,5]))
    #print(LCM([2,4,3]))
    #print(LCM([2,3,7]))
    #print(LCM([2, 7, 3, 9, 4]))

    '''
    str='restart'
    ch=str[0]
    fnl=[]
    fnl.append(ch)
    for i in range(1,len(str)):
        if str[i]==ch:
            fnl.append('$')
        else:
            fnl.append(str[i])
    print(''.join(fnl))
    '''
    '''

    lst=["PHP", "Exercises", "Backend"]
    max=-999
    for l in lst:
        if len(l)>max:
            max=len(l)
    print(max)
    '''

    #str='red, white, black, red, green, black'
    #lst=str.split(',')
    #print(sorted(set(lst)))

    #lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    #print(sorted(lst,key=lambda x:x[1]))

    #dict={1:2}
    #print(len(dict))

    #lst1 = [3, 4, 6, 10, 11, 18]
    #lst2 = [1, 5, 7, 12, 13, 19, 21]
    #print(MergeList(lst1,lst2))

    tup_list = [(0, 15), (20, 25), (40, 50), (10, 30), (45, 54), (55, 65)]
    print(MovieTimes(tup_list))


if __name__=='__main__':
    main()
