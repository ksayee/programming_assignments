'''
Input : arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
Output : 2 5

Input : arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125 ], x = 7
Output : 6 6

Input: arr[] = [1, 2, 3], x = 4
Output: -1 -1
'''

def binary_search(input_lst,element,find_first_flg):

        low=0
        high = len(input_lst)-1

        idx = -1
        while low <= high:
                mid = (low + high)//2

                if input_lst[mid] == element:
                        idx = mid
                        if find_first_flg is True:
                                high = mid -1
                        else:
                                low = mid +1
                elif input_lst[mid] < element:
                        low = mid + 1
                else:
                        high = mid -1

        return idx

def GetFirstLastSortedArray(input_lst,element):
        output_lst=[]

        first_idx = binary_search(input_lst,element,find_first_flg = True)
        last_idx = binary_search(input_lst, element, find_first_flg =False)

        output_lst.append(first_idx)
        output_lst.append(last_idx)

        return output_lst


def main():
        input_lst=[1, 3, 5, 5, 5, 5, 67, 123, 125]
        element = 5
        print(GetFirstLastSortedArray(input_lst,element))

        input_lst = [1, 3, 5, 5, 5, 5, 7, 123, 125 ]
        element = 7
        print(GetFirstLastSortedArray(input_lst, element))

        input_lst = [1, 2, 3]
        element = 4
        print(GetFirstLastSortedArray(input_lst, element))

if __name__ == '__main__':
        main()