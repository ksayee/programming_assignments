import collections

def StructureString(str1):

    lst=[]
    lst=str1.split()
    return ' '.join(lst)

def UniqueNum(n):

    lst={}

    while n!=0:
        key=n%10
        if key in lst.keys():
            return False
        else:
            lst[key]=1
        n=int(n/10)

    return True

def LetterUnique(str1):

    tmp_lst=collections.Counter(str1).most_common()
    lst=list(filter(lambda x:x[1]>1,tmp_lst))
    if len(lst)>0:
        return False
    else:
        return True

def main():
    #str1 = '       I work          in Amazon in Seattle       I           life         '
    #print(StructureString(str1))

    #n = 1000
    #print(UniqueNum(n))

    #str1 = 'mary'
    #print(LetterUnique(str1))

    lst1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    A = 'aacde'
    tmp=A.replace('a','')
    print(tmp)



if __name__=='__main__':
    main()
