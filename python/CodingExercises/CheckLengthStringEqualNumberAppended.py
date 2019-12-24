'''
Check length of a string is equal to the number appended at its last
Given a string that (may) be appended with a number at last.
You need to find whether the length of string excluding that number is equal to that number.
 For example for “helloworld10”, answer is True as helloworld consist of 10 letters. Length of String is less than 10, 000.

Examples :

Input:  str = "geeks5"
Output:  Yes
Explanation : As geeks is of 5 length and at
              last number is also 5.

Input:  str = "geeksforgeeks15"
Explanation: As geeksforgeeks is of 13 length and
             at last number is 15 i.e. not equal
'''

def CheckLenghtStringEqualNumberAppended(str1):

    num_lst=[]
    for i in range(len(str1)-1,-1,-1):
        key=str1[i]
        if key>='0' and key<='9':
            num_lst.insert(0,key)
        else:
            break
    if len(str1[:i+1])==int(''.join(num_lst)):
        return True
    else:
        return False


def main():

    str1='geeks5'
    print(CheckLenghtStringEqualNumberAppended(str1))

    str1 = 'helloworld10'
    print(CheckLenghtStringEqualNumberAppended(str1))

    str1 = 'geeksforgeeks15'
    print(CheckLenghtStringEqualNumberAppended(str1))

if __name__=='__main__':
    main()