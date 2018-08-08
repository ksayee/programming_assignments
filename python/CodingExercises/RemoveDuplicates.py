# Remove all duplicates from a given string in Python
# We are given a string and we need to remove all duplicates from it ? What will be the output if order of character matters ?

def RemoveDuplicates(str1):

    fnl_lst=[]

    for i in range(0,len(str1)):

        key=str1[i]

        if len(fnl_lst)==0:
            fnl_lst.append(key)
        elif key not in fnl_lst:
            fnl_lst.append(key)
        else:
            continue

    return ''.join(fnl_lst)

def main():

    str1='geeksforgeeks'
    print(RemoveDuplicates(str1))

if __name__=='__main__':
    main()