'''
472. Concatenated Words
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
'''

def Validate(key,input_ary):

    word_lst=key.split(',')
    if len(word_lst)==1:
        return False

    flg=True
    i=0
    for word in word_lst:
        if word in input_ary:
            i=i+1
        else:
            flg=False
            break
    if i>1 and flg==True:
        return True
    else:
        return False

def Combinations_recur(lst,tmp,idx,op_idx,out_lst,input_ary):

    if idx==len(lst):
        flg=Validate(''.join(tmp).strip(','),input_ary)
        if flg==True:
            out_lst.append(''.join(tmp).strip(','))
        return

    tmp[op_idx]=lst[idx]
    tmp[op_idx+1]=','
    Combinations_recur(lst, tmp, idx+1, op_idx+2, out_lst,input_ary)

    if idx+1<len(lst):
        Combinations_recur(lst, tmp, idx+1, op_idx+1, out_lst,input_ary)

def LeetCode472(ary):

    fnl_lst=[]
    for word in ary:
        lst=list(word)
        tmp=[0]*(len(lst)*2)
        idx=0
        op_idx=0
        out_lst=[]
        input_ary=ary
        Combinations_recur(lst,tmp,idx,op_idx,out_lst,input_ary)
        for key in out_lst:
            fnl_lst.append(key.replace(',',''))
    return fnl_lst

def main():

    ary=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print(LeetCode472(ary))

if __name__=='__main__':
    main()