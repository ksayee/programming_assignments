
def Validate(tmp_str,word_lst):

    for item in tmp_str.split(','):
        if item not in word_lst:
            return False
    return True

def Combinations_recur(input_str,tmp_lst,idx,op_idx,output_lst,word_lst):

    if idx==len(input_str):
        flg = Validate(''.join(tmp_lst).strip(','),word_lst)
        if flg is True:
            output_lst.append(''.join(tmp_lst).strip(',').replace(',',' '))
        return

    tmp_lst[op_idx]= input_str[idx]
    tmp_lst[op_idx + 1] =','
    Combinations_recur(input_str,tmp_lst,idx+1,op_idx+2,output_lst,word_lst)
    if idx+1 < len(input_str):
        Combinations_recur(input_str, tmp_lst, idx + 1, op_idx + 1, output_lst,word_lst)

def Solution(input_str,word_lst):

    tmp_lst=[0] * len(input_str) * 2

    idx=0
    op_idx=0
    output_lst=[]

    Combinations_recur(input_str,tmp_lst,idx,op_idx,output_lst,word_lst)
    return output_lst


def main():

    input_str = "catsanddog"
    word_lst = ["cat", "cats", "and", "sand", "dog"]
    print(Solution(input_str, word_lst))

    input_str = "pineapplepenapple"
    word_lst = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(Solution(input_str, word_lst))

if __name__=='__main__':
    main()