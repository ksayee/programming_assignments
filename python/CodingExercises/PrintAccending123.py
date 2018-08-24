# Print number in ascending order which contains 1, 2 and 3 in their digits.
# Given an array of numbers, the task is to print those numbers in ascending order separated by commas which have 1, 2 and 3 in their digits. If no number containing digits 1, 2, and 3 present then print -1.

def PrintAccending123(ary):

    lst=list(ary)
    n='123'
    fnl_lst=[]
    for l in lst:
        tmp=sorted(set(str(l)))
        if n==''.join(tmp)[:3]:
            fnl_lst.append(l)

    if len(fnl_lst)>1:
        fnl_lst.sort()
        return fnl_lst
    else:
        return -1

def main():

    ary=[123, 1232, 456, 234, 32145]
    print(PrintAccending123(ary))

    ary = [9821, 627183, 12, 1234]
    print(PrintAccending123(ary))

    ary = [12, 232, 456, 234]
    print(PrintAccending123(ary))

if __name__=='__main__':
    main()