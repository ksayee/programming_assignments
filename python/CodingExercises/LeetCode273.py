'''
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
Example 1:
Input: 123
Output: "One Hundred Twenty Three"
Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

def LeetCode273(num):

    dict={}
    dict[0]='Zero'
    dict[1] = 'One'
    dict[2] = 'Two'
    dict[3] = 'Three'
    dict[4] = 'Four'
    dict[5] = 'Five'
    dict[6] = 'Six'
    dict[7] = 'Seven'
    dict[8] = 'Eight'
    dict[9] = 'Nine'
    dict[10] = 'Ten'
    dict[11] = 'Eleven'
    dict[12] = 'Twelve'
    dict[13] = 'Thirteen'
    dict[14] = 'Fourteen'
    dict[15] = 'Fifteen'
    dict[16] = 'Sixteen'
    dict[17] = 'Seventeen'
    dict[18] = 'Eightteen'
    dict[19] = 'Nineteen'
    dict[20] = 'Twenty'
    dict[30] = 'Thirty'
    dict[40] = 'Fourty'
    dict[50] = 'Fifty'
    dict[60] = 'Sixty'
    dict[70] = 'Seventy'
    dict[80] = 'Eighty'
    dict[90] = 'Ninety'
    dict[100] = 'Hundred'
    dict[1000] = 'Thousand'
    dict[100000] = 'Million'
    dict[10000000] = 'Billion'

    output_lst=[]
    done_lst=[]
    tmp=1
    while num!=0:
        rem=num%10
        if rem!=0:
            if tmp==1:
                output_lst.insert(0,dict[rem])
            elif tmp==10:
                if rem==1:
                    if len(output_lst)!=0:
                        prev_num=output_lst[0]
                    else:
                        prev_num=0
                    curr_num=rem*10+prev_num
                    output_lst.pop()
                    output_lst.insert(0,dict[curr_num])
                else:
                    curr_num=rem*tmp
                    output_lst.insert(0,dict[curr_num])
            elif tmp==10000:
                if done_lst[-1]!=0:
                    output_lst.pop(0)
                    output_lst.pop(0)
                if rem==1:
                    curr_num=rem*10+done_lst[-1]*1
                    output_lst.insert(0,dict[1000])
                    output_lst.insert(0,dict[curr_num])
                else:
                    output_lst.insert(0, dict[1000])
                    if done_lst[-1]!=0:
                        output_lst.insert(0,dict[done_lst[-1]])
                    output_lst.insert(0,dict[rem*10])

            else:
                output_lst.insert(0,dict[tmp])
                output_lst.insert(0,dict[rem])
        tmp=tmp*10
        num=num//10
        done_lst.append(rem)

    return ' '.join(output_lst)

def main():

    num=123
    print(LeetCode273(num))

    num = 12345
    print(LeetCode273(num))

    num = 300
    print(LeetCode273(num))

    num = 301
    print(LeetCode273(num))

    num = 563
    print(LeetCode273(num))

    num = 3563
    print(LeetCode273(num))

    num = 30563
    print(LeetCode273(num))

if __name__=='__main__':
    main()