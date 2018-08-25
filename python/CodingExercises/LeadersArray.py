# Leaders in an array
# Write a program to print all the LEADERS in the array.
# An element is leader if it is greater than all the elements to its right side.
# And the rightmost element is always a leader.
# For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

def LeadersArray(ary):

    fnl_lst=[]

    max_num=ary[len(ary)-1]

    fnl_lst.append(max_num)

    for i in range(len(ary)-2,-1,-1):

        key=ary[i]
        if key>max_num:
            fnl_lst.append(key)
            max_num=key

    fnl_lst.reverse()
    return fnl_lst

def main():
    
    ary=[16, 17, 4, 3, 5, 2]
    print(LeadersArray(ary))

if __name__=='__main__':
    main()