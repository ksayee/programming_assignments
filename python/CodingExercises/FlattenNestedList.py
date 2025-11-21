
def FlattenList_recur(input_lst,output_lst):
    for item in input_lst:
        if isinstance(item,list):
            FlattenList_recur(item,output_lst)
        else:
            output_lst.append(item)

def Solution(input_lst):

    output_lst = []

    for item in input_lst:
        if isinstance(item,list):
            FlattenList_recur(item,output_lst)
        else:
            output_lst.append(item)
    return output_lst

def main():

    input_lst=[1, [2, [3, 4], 5], [6,7,[8,[9,[10,[11,[12]]]]]]]
    print(Solution(input_lst))

if __name__=='__main__':
    main()