'''
String with additive sequence
Given a string, the task is to find whether it contains an additive sequence or not.
A string contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers.
A valid string should contain at least three digit to make one additive sequence.
Examples:
Input : s = “235813”
Output : true
2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13

Input : s = “199100199”
Output : true
1 + 99 = 100, 99 + 100 = 199

Input : s = “12345678”
Output : false
'''

def Validate(num_str):

    lst=num_str.split(',')
    if len(lst)>2:
        for i in range(2,len(lst)):
            key=int(lst[i])
            if key==int(lst[i-1])+int(lst[i-2]):
                pass
            else:
                return False
        return True
    else:
        return False

def Combinations_recur(tmp,idx,op_idx,output_lst,word):

    if idx==len(word):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            output_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, output_lst, word)

    if idx+1<len(word):
        Combinations_recur(tmp, idx+1, op_idx+1, output_lst, word)

def AdditiveSequence(word):

    tmp=[0]*len(word)*2
    idx=0
    op_idx=0
    output_lst=[]
    Combinations_recur(tmp,idx,op_idx,output_lst,word)
    return output_lst

def main():

    word='235813'
    print(AdditiveSequence(word))

    word = '199100199'
    print(AdditiveSequence(word))

    word='12345678'
    print(AdditiveSequence(word))

if __name__=='__main__':
    main()