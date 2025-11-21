
def Validate(tmp_str,input_dict):

    tmp=[]
    for item in tmp_str.split(','):
        if item not in input_dict:
            return False, ()
        tmp.append(input_dict[item])

    tup = (tmp_str,','.join(tmp))

    return True,tup
def Combinations_recur(input_dict,input_str,tmp_lst,idx,op_idx,output_lst):

    if idx==len(input_str):
        flg,tup = Validate(''.join(tmp_lst).strip(','),input_dict)
        if flg is True:
            output_lst.append(tup)
        return

    tmp_lst[op_idx] = input_str[idx]
    tmp_lst[op_idx+1] = ','

    Combinations_recur(input_dict, input_str, tmp_lst, idx+1, op_idx+2, output_lst)

    if idx+1<len(input_str):
        Combinations_recur(input_dict, input_str, tmp_lst, idx+1, op_idx+1, output_lst)
def Solution(input_dict,input_str):

    tmp_lst=[0] * len(input_str) *2

    idx=0
    op_idx=0
    output_lst=[]

    Combinations_recur(input_dict,input_str,tmp_lst,idx,op_idx,output_lst)

    print("Input String: ",input_str)
    print("Output String: ")
    for item in output_lst:
        print(item)

def main():
    input_dict = {
        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "E",
        "6": "F",
        "7": "G",
        "8": "H",
        "9": "I",
        "10": "J",
        "11": "K",
        "12": "L",
        "13": "M",
        "14": "N",
        "15": "O",
        "16": "P",
        "17": "Q",
        "18": "R",
        "19": "S",
        "20": "T",
        "21": "U",
        "22": "V",
        "23": "W",
        "24": "X",
        "25": "Y",
        "26": "Z"
    }
    input_str='226'
    Solution(input_dict,input_str)

    input_str = '12'
    Solution(input_dict, input_str)

    input_str = '06'
    Solution(input_dict, input_str)

    input_str = '11106'
    Solution(input_dict, input_str)

if __name__=='__main__':
    main()