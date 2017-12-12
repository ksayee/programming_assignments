
def arraypairsum(ary,sum):

    lst={}

    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    for i in range(0,len(ary)):
        tmp=sum-ary[i]
        if tmp in lst.keys():
            lst[tmp]=lst.get(tmp)-1
            lst[ary[i]]=lst.get(ary[i])-1
            if lst.get(tmp)==0:
                del lst[tmp]
            if lst.get(ary[i])==0:
                del lst[ary[i]]
            print('The numbers are:',ary[i],tmp)
        else:
            continue


def main():
    ary=[1, 5, 7, -1]
    sum=6

    arraypairsum(ary,sum)

    ary = [1, 5, 7, -1, 5]
    sum = 6
    arraypairsum(ary,sum)

if __name__=='__main__':
    main()
