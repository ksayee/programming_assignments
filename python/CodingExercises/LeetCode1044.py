'''
1044. Longest Duplicate Substring
Hard
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.
(The occurrences may overlap.)
Return any duplicated substring that has the longest possible length.
(If S does not have a duplicated substring, the answer is "".)
Example 1:
Input: "banana"
Output: "ana"
Example 2:
Input: "abcd"
Output: ""
'''

def Validate(sub_str,word,fnl_lst):

    chk_lst=sub_str.split(',')
    temp_word=word
    for check_word in chk_lst:
        if len(check_word)>1:
            flg=False
            temp_word=word
            cnt=0
            while True:
                try:
                    idx=temp_word.index(check_word)
                    temp_word=temp_word[idx+1:]
                    cnt=cnt+1
                    if cnt==2:
                        flg=True
                        break
                except:
                    break
            if flg==True:
                if check_word not in fnl_lst:
                    fnl_lst.append(check_word)

def Combinations_recur(tmp,fnl_lst,idx,op_idx,word):

    if idx==len(word):
        Validate(''.join(tmp).strip(','),word,fnl_lst)
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, fnl_lst, idx+1, op_idx+2, word)

    if idx+1<len(word):
        Combinations_recur(tmp, fnl_lst, idx+1, op_idx+1, word)

def LeetCode1044(word):

    tmp=[0]*(2*len(word))

    idx=0
    op_idx=0
    fnl_lst=[]
    Combinations_recur(tmp,fnl_lst,idx,op_idx,word)
    if len(fnl_lst)==0:
        return 'NONE'
    else:
        return sorted(fnl_lst,key=lambda x:len(x),reverse=True)[0]

def main():

    word='banana'
    print(LeetCode1044(word))

    word = 'abcd'
    print(LeetCode1044(word))

if __name__=='__main__':
    main()