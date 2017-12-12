def SingleOccurence(ary):

    lst={}
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys() and lst.get(key)==1:
            fnl_lst.append(key)
        else:
            continue
    print(fnl_lst)

def main():
    ary = [1,2,2,7,9,4,9,4,85,6,34,6,1,10,34,45]
    SingleOccurence(ary)

if __name__=='__main__':
    main()