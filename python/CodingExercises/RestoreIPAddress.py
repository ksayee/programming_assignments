
def Validate(tmp_str):

    if len(tmp_str.split(',')) < 4 or len(tmp_str.split(',')) > 4:
        return False

    for num in tmp_str.split(','):
        if int(num) < 0 or int(num) > 255:
            return False
    return True

def combinations_recur(input_str,tmp_lst,idx,op_idx,output_lst):

    if idx == len(input_str):
        flg = Validate(''.join(tmp_lst).strip(','))
        if flg is True:
            output_lst.append(''.join(tmp_lst).strip(','))
        return

    tmp_lst[op_idx]=input_str[idx]
    tmp_lst[op_idx+1]=','
    combinations_recur(input_str, tmp_lst, idx+1, op_idx+2, output_lst)

    if idx +1 <len(input_str):
        combinations_recur(input_str, tmp_lst, idx + 1, op_idx + 1, output_lst)

def Solution(input_str):

    tmp_lst = [0] * len(input_str) * 2

    idx=0
    op_idx = 0
    output_lst=[]

    combinations_recur(input_str,tmp_lst,idx,op_idx,output_lst)
    return output_lst


def main():

    input_str='25525511135'
    print(Solution(input_str))

if __name__=='__main__':
    main()