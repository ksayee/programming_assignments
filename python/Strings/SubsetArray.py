
def subsetarray(ary1,ary2):

    if len(ary1)>len(ary2):
        max_ary=ary1
        min_ary=ary2
    else:
        max_ary=ary2
        min_ary=ary1

    lst={}
    flg=True
    for i in range(0,len(max_ary)):

        key=max_ary[i]
        if key in lst.keys():
            lst[key]=1
        else:
            lst[key]=1

    for j in range(0,len(min_ary)):
        key=min_ary[j]
        if key in lst.keys():
            continue
        else:
            flg=False
            break

    if flg==True:
        print('The Smaller array is indeed subset of Bigger array')
        print(max_ary)
        print(min_ary)
    else:
        print('The Smaller array is NOT subset of Bigger array')
        print(max_ary)
        print(min_ary)

def main():

    ary1=[11, 1, 13, 21, 3, 7]
    ary2=[11, 3, 7, 1]

    subsetarray(ary1,ary2)

    ary1 = [1, 2, 3, 4, 5, 6]
    ary2 = [1, 2, 4]

    subsetarray(ary1, ary2)

    ary1 = [10, 5, 2, 23, 19]
    ary2 = [19, 5, 3]

    subsetarray(ary1, ary2)


if __name__=='__main__':
    main()
