# Ceiling in a sorted array
# Given a sorted array and a value x,
# the ceiling of x is the smallest element in array greater than or equal to x,
# and the floor is the greatest element smaller than or equal to x.
# Assume than the array is sorted in non-decreasing order.
# Write efficient functions to find floor and ceiling of x.

def FloorCielingArray(ary,k):

    fnl_lst=[]

    for i in range(0,len(ary)):

        if ary[i] == k:
            fnl_lst.append('Floor is: ' + str(ary[i]))
            fnl_lst.append('Cieling is: ' + str(ary[i]))
            break
        elif i==0:
            if ary[i]>k:
                fnl_lst.append('No Floor')
                fnl_lst.append('Cieling is: '+str(ary[i]))
                break
        elif i==len(ary)-1:
            if ary[i]<k:
                fnl_lst.append('Floor is: ' + str(ary[i]))
                fnl_lst.append('No Cieling')
                break
        else:
            if k>ary[i-1] and k<ary[i]:
                fnl_lst.append('Floor is: ' + str(ary[i-1]))
                fnl_lst.append('Cieling is: ' + str(ary[i]))
                break

    return fnl_lst

def main():
    
    ary=[1, 2, 8, 10, 10, 12, 19]
    k=0
    print(FloorCielingArray(ary,k))

    k = 1
    print(FloorCielingArray(ary,k))

    k = 3
    print(FloorCielingArray(ary,k))

    k = 5
    print(FloorCielingArray(ary,k))

    k = 20
    print(FloorCielingArray(ary,k))

if __name__=='__main__':
    main()