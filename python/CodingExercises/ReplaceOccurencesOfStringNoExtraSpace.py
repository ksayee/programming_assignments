'''
Replace all occurrences of string AB with C without using extra space
Given a string str that may contain one more occurrences of “AB”. Replace all occurrences of “AB” with “C” in str.

Examples:

Input  : str = "helloABworld"
Output : str = "helloCworld"

Input  : str = "fghABsdfABysu"
Output : str = "fghCsdfCysu"
'''

def ReplaceOccurencesOfStringNoExtraSpace(str1):

    flg=False
    for i in range(0,len(str1)):
        key=str1[i]
        if key=='A':
            flg=True
        elif key=='B':
            if flg==True:
                str1=str1[:i-1]+'C'+' '+str1[i+1:]
                flg=False
        else:
            flg=False
    return str1.replace(' ','')

def main():
    
    str1="helloABworld"
    print(ReplaceOccurencesOfStringNoExtraSpace(str1))

    str1 = "fghABsdfABysu"
    print(ReplaceOccurencesOfStringNoExtraSpace(str1))

if __name__=='__main__':
    main()