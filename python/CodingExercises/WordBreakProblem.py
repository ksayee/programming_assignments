'''
Word Break Problem using Backtracking
Given a valid sentence without any spaces between the words and a dictionary of valid English words, find all possible ways to break the sentence in individual dictionary words.

Example

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input: "ilikesamsungmobile"
Output: i like sam sung mobile
        i like samsung mobile

Input: "ilikeicecreamandmango"
Output: i like ice cream and man go
        i like ice cream and mango
        i like icecream and man go
        i like icecream and mango
'''

def Validate(str1,ary):
    words=str1.split(',')
    for word in words:
        if word not in ary:
            return False
    return True

def Combinations_recur(tmp,idx,op_idx,input_str,ary,output_lst):

    if idx==len(input_str):
        flg=Validate(''.join(tmp).strip(','),ary)
        if flg==True:
            output_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[op_idx]=input_str[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, input_str,ary,output_lst)

    if idx+1<len(input_str):
        Combinations_recur(tmp, idx+1, op_idx+1, input_str,ary,output_lst)

def WordBreakProblem(ary, input_str):

    tmp=[0]*len(input_str)*2
    idx=0
    op_idx=0
    output_lst=[]
    Combinations_recur(tmp,idx,op_idx,input_str,ary,output_lst)
    return output_lst

def main():

    ary=['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice','cream', 'icecream', 'man', 'go', 'mango','and']
    input_str='ilikesamsungmobile'
    print(WordBreakProblem(ary,input_str))

    input_str = 'ilikeicecreamandmango'
    print(WordBreakProblem(ary, input_str))

    input_str = 'ilike'
    print(WordBreakProblem(ary, input_str))

    input_str = 'ilikesamsung'
    print(WordBreakProblem(ary, input_str))

if __name__=='__main__':
    main()