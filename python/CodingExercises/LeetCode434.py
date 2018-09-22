'''
434. Number of Segments in a String
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''

def LeetCode434(str1):

    lst=str1.split()

    return len(lst)

def main():

    str1='Hello, my name is John'
    print(LeetCode434(str1))

if __name__=='__main__':
    main()