'''
Program to generate all possible valid IP addresses from given string
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
Examples :
Input : 25525511135
Output : [“255.255.11.135”, “255.255.111.35”]
Explanation:
These are the only valid possible
IP addresses.
Input : "25505011535"
Output : []
Explanation :
We cannot generate a valid IP
address with this string.
'''

def Validate(num_str):

    lst=num_str.split(',')
    if len(lst)!=4:
        return False
    for key in lst:
        if int(key)>=0 and int(key)<=255:
            pass
        else:
            return False
    return True

def Combinations_recur(tmp,idx,op_idx,word,output_lst):

    if idx==len(word):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            output_lst.append(''.join(tmp).strip(','))
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, word, output_lst)

    if idx+1<len(word):
        Combinations_recur(tmp, idx+1, op_idx+1, word, output_lst)

def GenerateAllPossibleValidIPAddressGivenString(word):

    tmp=[0]*len(word)*2
    idx=0
    op_idx=0
    output_lst=[]
    Combinations_recur(tmp,idx,op_idx,word,output_lst)
    return output_lst

def main():

    word='25525511135'
    print(GenerateAllPossibleValidIPAddressGivenString(word))

    word = '25505011535'
    print(GenerateAllPossibleValidIPAddressGivenString(word))

if __name__=='__main__':
    main()