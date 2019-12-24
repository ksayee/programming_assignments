'''
Decode a string recursively encoded as count followed by substring
An encoded string (s) is given, the task is to decode it.
The pattern in which the strings are encoded is as follows.
<count>[sub_str] ==> The substring 'sub_str'
                      appears count times.
Examples:
Input : str[] = "1[b]"
Output : b
Input : str[] = "2[ab]"
Output : abab
Input : str[] = "2[a2[b]]"
Output : abbabb
Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca
'''

def DecodeString(str1):

    stk=[]
    output_list=[]
    for i in range(0,len(str1)):
        key=str1[i]
        if key==']':
            while stk[-1]!='[':
                output_list.insert(0,stk[-1])
                stk.pop()
            stk.pop()
            num=int(stk[-1])
            stk.pop()
            word=''.join(output_list)
            output_list=[]
            while num>0:
                output_list.append(word)
                num=num-1
        else:
            stk.append(key)
    return ''.join(output_list)

def main():

    str1='1[b]'
    print(DecodeString(str1))

    str1 = '2[ab]'
    print(DecodeString(str1))

    str1 = '2[a2[b]]'
    print(DecodeString(str1))

    str1 = '3[b2[ca]]'
    print(DecodeString(str1))

if __name__=='__main__':
    main()