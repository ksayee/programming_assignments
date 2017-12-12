def RemoveDuplicates(ary):

    lst={}
    cnt=0
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1
            cnt=cnt+1

    print(cnt)

def main():

    ary=[1,1,1,2,2,3,5,5,7,7,7,8,9,10,34,34,56,56,56]
    RemoveDuplicates(ary)

if __name__=='__main__':
    main()