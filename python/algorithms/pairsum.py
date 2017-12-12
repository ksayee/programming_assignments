
def pairsum(ary,sm):

    lst={}

    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    for i in range(0,len(ary)):
        key=sm-ary[i]
        if key in lst.keys() and key==ary[i] and lst.get(key)>1:
            print('The 2 numbers are:',ary[i],key)
            lst[key]=lst.get(key)-1
        elif key in lst.keys() and key!=ary[i] and lst.get(key)==1:
            print('The 2 numbers are:', ary[i], key)
            lst[key] = lst.get(key) - 1
            lst[ary[i]]=lst.get(ary[i])-1
        else:
            continue

def main():

    ary=[2,5,3,7,9,5,5,0,8]
    x=10
    print(ary)
    print('Sum: ',x)
    pairsum(ary,x)

if __name__=='__main__':
    main()
