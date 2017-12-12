def lettercount(str1):

    count=0
    lst={}
    for i in range(0,len(str1)):
        if str1[i]!=' ' and ((str1[i]>='a' and str1[i]<='z') or (str1[i]>='A' and str1[i]<='Z')):
            key=str1[i]
            if key in lst.keys():
                lst[key]=lst.get(key)+1
            else:
                lst[key]=1

    for key,val in lst.items():
        print(key,val)

def main():
    str1 = 'I work in Amazon in Seattle'

    lettercount(str1)


if __name__=='__main__':
    main()
