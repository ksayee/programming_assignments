'''
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''


def reverseString(s):
    return ''.join(list(reversed(s)))

def main():
    s = "hello"
    print(reverseString(s))

if __name__=='__main__':
    main()