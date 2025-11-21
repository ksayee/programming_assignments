
import collections

def Validate(tmp_str,phone,num):

    num_str = str(num)

    for i in range(0,len(tmp_str)):
        if tmp_str[i] not in phone[int(num_str[i])]:
            return False
    return True

def combinations_recur(lst,cnt,tmp_lst,output_lst,phone,digit_cnt,num):

    if len(tmp_lst)== digit_cnt:
        flg = Validate(''.join(tmp_lst),phone,num)
        if flg is True:
            output_lst.append(''.join(tmp_lst))

    for i in range(0,len(lst)):
        if cnt[i] == 0:
            continue
        tmp_lst.append(lst[i])
        cnt[i] = cnt[i] -1
        combinations_recur(lst, cnt, tmp_lst, output_lst, phone,digit_cnt,num)
        tmp_lst.pop()
        cnt[i] = cnt[i] + 1

def Solution(phone, num):

    tmp_num = num
    digit_cnt =0

    input_lst=[]

    while tmp_num !=0:
        rem = tmp_num %10
        tmp_num = tmp_num//10
        digit_cnt = digit_cnt +1

        if rem in phone.keys():
            input_lst.append(phone[rem])

    dict = collections.Counter(''.join(input_lst))

    lst=[]
    cnt=[]
    tmp_lst=[]
    output_lst=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    combinations_recur(lst,cnt,tmp_lst,output_lst,phone,digit_cnt, num)

    return output_lst

def main():

    phone = {
        2: "abc", 3: "def", 4: "ghi", 5: "jkl",
        6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
    }
    num = 23
    print(Solution(phone, num))

    num = 79
    print(Solution(phone, num))

    num = 223
    print(Solution(phone, num))

if __name__=='__main__':
    main()