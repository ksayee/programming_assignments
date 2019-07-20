'''
1108. Defanging an IP Address
Easy
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''

def LeetCode1108(address):

    lst=address.split('.')
    return '[.]'.join(lst)

def main():

    address="1.1.1.1"
    print(LeetCode1108(address))

    address = "255.100.50.0"
    print(LeetCode1108(address))

if __name__=='__main__':
    main()