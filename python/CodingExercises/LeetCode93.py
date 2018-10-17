'''
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

def LeetCode93(str1):

    tmp=[0]*(len(str1)*2)
    fnl_lst=[]
    idx=0
    op_idx=0
    Combinations_recur(str1, tmp, fnl_lst,idx,op_idx)

    return fnl_lst

def Validate(ip):

    flg=True

    if len(ip.split('.'))!=4:
        return False
    else:
        lst=ip.split('.')
        for key in lst:
            if len(key)<=3:
                if int(key)>=0 and int(key)<=255:
                    continue
                else:
                    return False
            else:
                return False
    return flg

def Combinations_recur(str1, tmp, fnl_lst, idx, op_idx):

    if idx==len(str1):
        flg=Validate(''.join(tmp).strip('.'))
        if flg==True:
            fnl_lst.append(''.join(tmp).strip('.'))
        return

    tmp[op_idx]=str1[idx]
    tmp[op_idx+1]='.'
    Combinations_recur(str1, tmp, fnl_lst, idx+1, op_idx+2)

    if idx+1<len(str1):
        Combinations_recur(str1, tmp, fnl_lst, idx + 1, op_idx + 1)

def main():
    
    str1='25525511135'
    print(LeetCode93(str1))

    str1 = '273351225'
    print(LeetCode93(str1))

    str1 = '25011255255'
    print(LeetCode93(str1))

if __name__=='__main__':
    main()