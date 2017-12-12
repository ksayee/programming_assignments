import random

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

            key=str1[st:end]
            if key in lst.keys():
                lst[key]=lst.get(key)+1
            else:
                lst[key]=1
            flg=True

        else:
            if flg==True:
                st=i
                flg=False

    for key, val in lst.items():
        print(key,val)

def unique(n):


    fnl_lst=[]

    for i in range(0,n):

        if i>9:
            tmp=i
            flg=False
            unq=True
            lst={}
            while(tmp!=0):
                key=tmp%10
                tmp=int(tmp/10)
                if key in lst.keys() and flg==True:
                    lst[key]=lst.get(key)+1
                elif flg==False:
                    lst[key]=1
                    flg=True
                else:
                    unq=False
                    break

            if unq==True:
                fnl_lst.append(i)
        else:
            continue

    print(fnl_lst)

def StructureString(str1):

    found=False
    sp_flg=False
    fnl_str=''
    for i in range(0,len(str1)):
        if str1[i]==' ' and found==False:
            continue
        elif str1[i]!=' ' and found==False:
            fnl_str=str1[i]
            found=True
        elif str1[i]!=' ' and found==True and sp_flg==False:
            fnl_str=fnl_str+str1[i]
        elif str1[i]!=' ' and found==True and sp_flg==True:
            fnl_str=fnl_str+' '+str1[i]
            sp_flg=False
        elif str1[i]==' ':
            sp_flg=True


    print(fnl_str)

def StringExpansion(str1):

    prev_chr=''
    fnl_str=''

    for i in range(0,len(str1)):
        if ord(str1[i])>=48 and ord(str1[i])<=57:
            n=int(str1[i])
            j=0
            while(j<n):
                if fnl_str=='':
                    fnl_str=prev_chr
                else:
                    fnl_str=fnl_str+prev_chr
                j=j+1
        else:
            prev_chr=str1[i]

    print(fnl_str)

def StringCompression(str1):

    prev_chr=str1[0]
    cnt=1
    fnl_str=''
    for i in range(1,len(str1)):
        if prev_chr!=str1[i]:
            if fnl_str == '':
                fnl_str = prev_chr+str(cnt)
            else:
                fnl_str = fnl_str + prev_chr+str(cnt)
            cnt=1
        else:
            cnt=cnt+1
        prev_chr=str1[i]

    fnl_str=fnl_str+prev_chr+str(cnt)

    print(fnl_str)

def plusone(ary,n):

    carry=n

    fnl=[]

    for i in range(len(ary)-1,-1,-1):

        val=ary[i]+carry
        fnl.append(str(val%10))
        carry=int(val/10)

    if carry>0:
        fnl.append(str(carry))
    fnl.reverse()

    print(''.join(fnl))



def fnl(s):
    return s[-1]

def rnd(i):
    return random.random()

def main():
    #str1 = 'I work in Amazon in Seattle I life'
    #WordCount(str1)
    #n=1000
    #unique(n)
    #str1='    This is Kartik   sayee from    Amazon    '
    #StructureString(str1)
    #str1='a3b1c5a2'
    #StringExpansion(str1)
    #str1='aabcccccaa'
    #StringCompression(str1)
    #ary=[9,9,7]
    #plusone(ary,8)

    #main_str='aabbccabab'
    #sub_str='ab'

    #print(main_str.count(sub_str))

    #strs = ['ccc', 'aaaa', 'd', 'bb']
    #print(sorted(strs,key=str.lower))

    strs = ['xc', 'zb', 'yd', 'wa']
    print(sorted(strs,key=fnl))

    tup=('hi',)
    print(tup[0])
    ary=[1,2,3,4,5,6,7,8,9]
    rtn=5

    print(sorted(ary,key=rnd)[:5])
    print(random.randrange(45,9458))



    tup=(3,4,5)
    tup=(1,2)+tup
    print(tup)

    str1='This is kartik sayee of Amazon working in Facebook'
    print(str1.split(' ',1))

if __name__=='__main__':
    main()