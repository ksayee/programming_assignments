'''

solution('__R__L_','___RL__') = True
solution('__R_L_','___LR__') = False
solution('__R','R__') = False

'''

def combinations_recur(input_str, idx, out_idx, tmp_lst, final_lst):

    if idx == len(input_str):
        final_lst.append(''.join(tmp_lst).strip('0').replace('0',''))
        print(final_lst)
        return

    if input_str[idx] in ('R','L'):
        if input_str[idx] == 'R':
            print(tmp_lst, input_str[idx], 'in R')
            if idx < len(input_str)-1:
                if input_str[idx+1] == '_':
                    if tmp_lst[out_idx+1] in ('_','0'):
                        tmp_lst[out_idx] = '_'
                        tmp_lst[out_idx+1] = 'R'
                    else:
                        tmp_lst[out_idx] = 'R'
                else:
                    tmp_lst[out_idx] = 'R'
            else:
                tmp_lst[out_idx] = 'R'
        elif input_str[idx] == 'L':
            print(tmp_lst, input_str[idx], 'in L')
            if idx > 0:
                if input_str[idx-1] == '_':
                    if tmp_lst[out_idx - 1] in ('_', '0'):
                        tmp_lst[out_idx] = '_'
                        tmp_lst[out_idx-1] = 'L'
                    else:
                        tmp_lst[out_idx] = 'L'
                else:
                    tmp_lst[out_idx] = 'L'
            else:
                tmp_lst[out_idx] = 'L'
    elif input_str[idx] == '_':
        print(tmp_lst, input_str[idx], 'in _')
        if tmp_lst[out_idx] in ('R','L'):
            pass
        else:
            tmp_lst[out_idx] = '_'

    print('finish',tmp_lst)

    combinations_recur(input_str, idx+1, out_idx+1, tmp_lst, final_lst)
    print('call back',tmp_lst,idx)

    if idx+1 < len(input_str):
        combinations_recur(input_str, idx+1 , out_idx, tmp_lst, final_lst)

def solution(input_str, output_str):

    tmp_lst = ['0'] * len(input_str)

    idx=0
    out_idx = 0

    final_lst =[]
    print(list(input_str))
    combinations_recur(input_str, idx, out_idx, tmp_lst, final_lst)
    print(final_lst)


def main():

    print(solution('_R_L', '_RL_'))
    #print(solution('__R__L_','___RL__'))
    #print(solution('__R_L_','___LR__'))
    #print(solution('__R','R__'))

if __name__=='__main__':
    main()