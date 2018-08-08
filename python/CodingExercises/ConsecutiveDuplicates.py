# Remove all consecutive duplicates from the string
# Given a string S, remove all the consecutive duplicates. Note that this problem is different from Recursively remove all adjacent duplicates. Here we keep one character and remove all subsequent same characters.def ConsecutiveDuplicates(str1):

def ConsecutiveDuplicates(str1):

    fnl_lst=[]

    for i in range(0,len(str1)):

        key=str1[i]

        if len(fnl_lst)==0:
            fnl_lst.append(key)
        elif key!=fnl_lst[-1]:
            fnl_lst.append(key)
        else:
            continue

    return ''.join(fnl_lst)

def main():

    str1='aaaaabbbbbb'
    print(ConsecutiveDuplicates(str1))

    str1 = 'geeksforgeeks'
    print(ConsecutiveDuplicates(str1))

    str1 = 'aabccba'
    print(ConsecutiveDuplicates(str1))


if __name__=='__main__':
    main()