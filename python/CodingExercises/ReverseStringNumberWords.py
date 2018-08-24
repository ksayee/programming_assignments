# Reverse String according to the number of words
# Given a string containing a number of words. If the count of words in string is even then reverse its even position’s words else reverse its odd position, push reversed words at the starting of a new string and append the remaining words as it is in order.

def ReverseStringNumberWords(str1):

    lst=str1.split()

    fnl_lst=[]

    if len(lst)%2==0:
        i=0
    else:
        i=1
    k=len(lst)-1
    while (k>=0):
        key=lst[k]
        tmp=list(key)
        tmp.reverse()
        fnl_lst.append(''.join(tmp))
        k=k-2

    while (i<=len(lst)-1):
        key=lst[i]
        fnl_lst.append(key)
        i=i+2

    return ' '.join(fnl_lst)

def main():

    str1='Ashish Yadav Abhishek Rajput Sunil Pundir'
    print(ReverseStringNumberWords(str1))

    str1 = 'Ashish Yadav Abhishek Rajput Sunil Pundir Prem'
    print(ReverseStringNumberWords(str1))

if __name__=='__main__':
    main()