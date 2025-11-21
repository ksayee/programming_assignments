
def Validate(tmp_str):

    for item in tmp_str.split(','):
        if len(item) == 1:
            pass
        elif len(item)>1:
            left = 0
            right = len(item)-1
            while left < right:
                if item[left] != item[right]:
                    return False
                left = left +1
                right = right -1
    return True

def combinations_recur(input_str,tmp_lst,idx,op_idx,output_lst):

    if idx == len(input_str):
        flg = Validate(''.join(tmp_lst).strip(','))
        if flg is True:
            output_lst.append(''.join(tmp_lst).strip(','))
        return

    tmp_lst[op_idx] = input_str[idx]
    tmp_lst[op_idx+1] = ','

    combinations_recur(input_str, tmp_lst, idx+1, op_idx+2, output_lst)

    if idx +1 <len(input_str):
        combinations_recur(input_str, tmp_lst, idx + 1, op_idx + 1, output_lst)


def Solution(input_str):

    tmp_lst=[0] * len(input_str) *2

    idx=0
    op_idx=0

    output_lst=[]

    combinations_recur(input_str,tmp_lst,idx,op_idx,output_lst)
    return output_lst

def main():

    input_str='aab'
    print(Solution(input_str))

    input_str = 'efe'
    print(Solution(input_str))

if __name__=='__main__':
    main()