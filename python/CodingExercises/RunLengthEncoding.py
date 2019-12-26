'''
Run Length Encoding
Given an input string, write a function that returns the Run Length Encoded string for the input string.
For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6”.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
a) Pick the first character from source string.
b) Append the picked character to the destination string.
c) Count the number of subsequent occurrences of the picked character and append the count to destination string.
d) Pick the next character and repeat steps b) c) and d) if end of string is NOT reached.
'''

def RunLenghtEncoding(str1):

    lst=[]
    curr=''
    prev=str1[0]
    cnt=1
    for i in range(1,len(str1)):
        curr=str1[i]
        if prev!=curr:
            lst.append(prev)
            lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    lst.append(prev)
    lst.append(str(cnt))
    return ''.join(lst)

def main():

    str1='wwwwaaadexxxxxx'
    print(RunLenghtEncoding(str1))

if __name__=='__main__':
    main()