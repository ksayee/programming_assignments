# Rearrange an array in maximum minimum form | Set 1
# Given a sorted array of positive integers, rearrange the array alternately i.e
# first element should be maximum value, second minimum value, third second max, fourth second min and so on.

def RearrangeArrayMaxMinForm(ary):

    lst=[0]*len(ary)

    min=0
    max=len(ary)-1

    flg=True
    for i in range(0,len(ary)):

        if flg==True:
            lst[i]=ary[max]
            max=max-1
            flg=False
        else:
            lst[i]=ary[min]
            min=min+1
            flg=True

    return lst

def main():

    ary=[1, 2, 3, 4, 5, 6, 7]
    print(RearrangeArrayMaxMinForm(ary))

    ary = [1, 2, 3, 4, 5, 6]
    print(RearrangeArrayMaxMinForm(ary))

if __name__=='__main__':
    main()