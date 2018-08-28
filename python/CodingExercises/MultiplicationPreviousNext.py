# Replace every array element by multiplication of previous and next
# Given an array of integers, update every element with multiplication of previous and next elements with following exceptions.
# a) First element is replaced by multiplication of first and second.
# b) Last element is replaced by multiplication of last and second last.

def MultiplicationPreviousNext(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):
        if i==0:
            fnl_lst.append(ary[i]*ary[i+1])
        elif i==len(ary)-1:
            fnl_lst.append(ary[i-1]*ary[i])
        else:
            fnl_lst.append(ary[i-1]*ary[i+1])

    return fnl_lst

def main():
    
    ary=[2, 3, 4, 5, 6]
    print(MultiplicationPreviousNext(ary))

if __name__=='__main__':
    main()