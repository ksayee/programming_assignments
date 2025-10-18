# Find pairs of numbers from the list which add up to the target sum. All pairs

def solution(input_lst,target_sum):

    output_lst=[]
    dict={}

    for i in range(0,len(input_lst)):
        num = input_lst[i]
        diff = target_sum - num
        if diff in dict.keys():
            for j in range(0,len(dict[diff])):
                tup = (input_lst[dict[diff][j]],num)
                output_lst.append(tup)
        if num in dict.keys():
            dict[num].append(i)
        else:
            dict[num] = []
            dict[num].append(i)

    return output_lst

def main():
    input_lst=[1,2,3,4,5,4,3,2,1]
    target_sum = 6
    print(solution(input_lst,target_sum))

if __name__=='__main__':
    main()

