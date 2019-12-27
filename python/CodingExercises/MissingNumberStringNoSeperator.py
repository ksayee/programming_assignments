'''
Find the missing number in a string of numbers with no separator
Given a string consisting of some numbers, not separated by any separator.
The numbers are positive integers and the sequence increases by one at each number except the missing number.
The task is to find the missing number. The numbers will have no more than six digits. Print -1 if input sequence is not valid.
Examples:
Input  : 89101113
Output : 12
Input  : 9899101102
Output : 100
Input  : 596597598600601602:
Output : 599
Input  : 909192939495969798100101
Output : 99
Input  : 11111211311411511
Output : -1
'''

def Validate(num_str):
    lst=num_str.split(',')
    miss_num=-1
    count=0
    if len(lst)==1:
        return (False,-1)
    for i in range(0,len(lst)):
        key=int(lst[i])
        if i==0:
            pass
        else:
            if key==next_num:
                pass
            elif key-next_num>1 or key-next_num<0:
                return (False,-1)
            else:
                miss_num=next_num
                count=count+1
                if count>1:
                    return (False,-1)
        next_num=key+1

    return (True,miss_num)

def Combinations_recur(tmp,idx,op_idx,output_list,word):

    if idx==len(word):
        tup=Validate(''.join(tmp).strip(','))
        if tup[0]==True:
            output_list.append(tup[1])
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, output_list, word)

    if idx+1<len(word):
        Combinations_recur(tmp, idx+1, op_idx+1, output_list, word)

def MissingNumberStringNoSeperator(word):

    tmp=[0]*len(word)*2

    idx=0
    op_idx=0
    output_list=[]
    Combinations_recur(tmp,idx,op_idx,output_list,word)
    return output_list

def main():

    word='89101113'
    print(MissingNumberStringNoSeperator(word))

    word = '9899101102'
    print(MissingNumberStringNoSeperator(word))

    word='596597598600601602'
    print(MissingNumberStringNoSeperator(word))

    word = '909192939495969798100101'
    print(MissingNumberStringNoSeperator(word))

if __name__=='__main__':
    main()