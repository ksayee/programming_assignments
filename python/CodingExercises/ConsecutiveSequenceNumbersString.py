'''
Consecutive sequenced numbers in a string
Given a string that contains only numeric digits, we need to check whether that strings contains numbers in consecutive sequential manner in increasing order.
Note: Negative numbers are not considered part of this problem. So we consider that input only contains positive integer.
Examples:

Input :  str = "1234"
Output : Yes
         1
Explanation :
There are 1, 2, 3, 4 which are
consecutive and in increasing order.
And the starting number is 1

Input :  str = "91012"
Output : No
Explanation :
There are no such sequence in the
string.

Input :  str = "99100"
Output : Yes
         99
Explanation : The consecutive sequential
numbers are 99, 100

Input :  str = "010203"
Output : NO
Explanation :
Although at first glance there seems to
be 01, 02, 03. But those wouldn't be
considered a number. 01 is not 1  it's 0, 1
'''

def Validate(num_str):
    lst=num_str.split(',')

    if len(lst)==1:
        return False

    for i in range(1,len(lst)):
        if int(lst[i])-int(lst[i-1])==1:
            pass
        else:
            return False
    return True

def Combination_recur(tmp,idx,op_idx,output_lst,word):

    if idx==len(word):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            output_lst.append(''.join(tmp).strip(','))
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combination_recur(tmp, idx+1, op_idx+2, output_lst, word)

    if idx+1<len(word):
        Combination_recur(tmp, idx+1, op_idx+1, output_lst, word)

def ConsecutiveSequenceNumbersString(word):

    tmp=[0]*len(word)*2
    idx=0
    op_idx=0
    output_lst=[]
    Combination_recur(tmp,idx,op_idx,output_lst,word)
    return output_lst


def main():

    word='1234'
    print(ConsecutiveSequenceNumbersString(word))

    word = '91012'
    print(ConsecutiveSequenceNumbersString(word))

    word = '99100'
    print(ConsecutiveSequenceNumbersString(word))

    word = '010203'
    print(ConsecutiveSequenceNumbersString(word))

if __name__=='__main__':
    main()