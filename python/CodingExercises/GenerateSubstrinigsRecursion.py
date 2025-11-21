

def GenerateSubstrings_recur(input_str,tmp_lst,start, end,output_lst):

    if end == len(input_str):
        tmp_str = input_str[start:end]
        if tmp_str not in output_lst:
            output_lst.append(tmp_str)
        return

    tmp_str= input_str[start:end]
    if tmp_str not in output_lst:
        output_lst.append(tmp_str)
    GenerateSubstrings_recur(input_str, tmp_lst, start, end +1, output_lst)
    GenerateSubstrings_recur(input_str, tmp_lst, start+1, start+2, output_lst)

def Solution(input_str):

    output_lst=[]
    start=0
    end=start +1
    tmp_lst=[]

    GenerateSubstrings_recur(input_str,tmp_lst,start, end,output_lst)
    return output_lst

def main():

    input_str='abc'
    print(Solution(input_str))

if __name__=='__main__':
    main()