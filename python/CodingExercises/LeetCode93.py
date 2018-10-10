'''
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

def LeetCode93(str1):

    fnl_lst=[]
    tmp=[]
    for i in range(0,len(str1)):

        key=str1[i]

        if len(tmp)<2:
            tmp.append(key)
        else:
            tmp.append(key)
            if int(''.join(tmp))<=255:
                fnl_lst.append(''.join(tmp))
                tmp=[]
            else:
                tmp.pop()
                fnl_lst.append(''.join(tmp))
                tmp=[]
                tmp.append(key)

    if len(tmp)>0:
        fnl_lst.append(''.join(tmp))

    return '.'.join(fnl_lst)


def main():
    
    str1='25525511135'
    print(LeetCode93(str1))

    str1 = '273351225'
    print(LeetCode93(str1))

    str1 = '25011255255'
    print(LeetCode93(str1))

if __name__=='__main__':
    main()