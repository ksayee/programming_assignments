'''
557. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''

def LeetCode557(str1):

    lst=str1.split()
    fnl_lst=[]

    for l in lst:
        fnl_lst.append(''.join(reversed(l)))
    return ' '.join(fnl_lst)

def DoReverse(str1):

    lst=list(str1)

    i=0
    j=len(lst)-1


    while i<j:
        tmp=lst[i]
        lst[i]=lst[j]
        lst[j]=tmp
        i=i+1
        j=j-1

    return ''.join(lst)

def LeetCode557_anotherSolution(str1):

    lst=list(str1)
    fnl_lst=[]

    flg=True
    for i in range(0,len(lst)):

        if i==len(lst)-1 or lst[i]==' ':
            if i==len(lst)-1:
                end=i+1
            else:
                end=i
            rev_tmp=DoReverse(''.join(lst[st:end]))
            fnl_lst.append(rev_tmp)
            flg=True
        else:
            if flg==True:
                st=i
                flg=False

    return ' '.join(fnl_lst)

def main():

    str1="Let's take LeetCode contest"
    print(LeetCode557(str1))
    print(LeetCode557_anotherSolution(str1))

if __name__=='__main__':
    main()