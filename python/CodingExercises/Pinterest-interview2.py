'''
Given a list of intervals, return a list of non overlapping intervals. If they are overlapping, merge them.
lst=[(1, 4), (3, 5), (6, 9), (8, 12)]
# -> [1, 5], [6, 12]
'''

def solution(input_lst):

    sorted_lst = sorted(input_lst, key=lambda x: x[0])
    output_lst = []

    output_lst.append(sorted_lst[0])
    k=0

    for i in range(1,len(sorted_lst)):
        tup = sorted_lst[i]
        if tup[0]<=output_lst[k][1]:
            if tup[1]<output_lst[k][1]:
                pass
            else:
                tmp_tup = (output_lst[k][0],tup[1])
                del output_lst[k]
                output_lst.append(tmp_tup)
        else:
            output_lst.append(tup)
            k=k+1

    return output_lst

def main():
    input_lst = [(1, 4), (3, 5), (6, 9), (8, 12)]
    print(solution(input_lst))

if __name__ == '__main__':
    main()