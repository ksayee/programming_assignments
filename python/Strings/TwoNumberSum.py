
def twonumbersum(ary,num):

    lst={}

    for i in range(0,len(ary)):

        key=num-ary[i]

        if key in lst.keys():
            print('The two numbers are:', key, ary[i])
        else:
            lst[ary[i]]=1

def main():
    ary=[1,4,45,6,10,8]
    num=12

    twonumbersum(ary,num)


if __name__=='__main__':
    main()
