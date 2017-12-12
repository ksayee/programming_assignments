# Given a string, write a progrom to extract all the valid IP addresses from the string and print them.

def validate(lst):
    num = 0
    flg = 0
    tmp_lst = []
    for i in range(0, len(lst)):
        if lst[i] != '.':
            num = (num*10)+int(lst[i])
            if i+1==len(lst):
                if num>265:
                    flg=1
        else:
            if num>265:
                flg=1
                break
            else:
                num=0

    if flg == 0:
        tmp_lst.append(''.join(lst))
    return tmp_lst

def ipaddress(str1):
    lst = []
    cnt = 0
    dot_cnt = 0
    tmp_lst = []
    fnl_lst = []
    for i in range(0, len(str1)):
        if dot_cnt == 3 and cnt == 3 or (dot_cnt == 3 and cnt == 3 and i+1==len(str1)):
            tmp_lst = validate(lst)
            if len(tmp_lst) != 0:
                fnl_lst.append(tmp_lst)
                lst = []
                cnt = 0
                dot_cnt = 0
        if (ord(str1[i]) >= 48 and ord(str1[i]) <= 57) or str1[i] == '.':
            if (i+1==len(str1) and dot_cnt==3):
                tmp_lst = validate(lst)
                if len(tmp_lst) != 0:
                    fnl_lst.append(tmp_lst)
            if (str1[i] == '.' and dot_cnt == 3):
                tmp_lst = validate(lst)
                if len(tmp_lst) != 0:
                    fnl_lst.append(tmp_lst)
                lst = []
                cnt = 0
                dot_cnt = 0
                continue
            elif str1[i] == '.' and dot_cnt < 3:
                dot_cnt = dot_cnt + 1
                cnt=0
                lst.append(str1[i])
            else:
                if cnt <= 2:
                    cnt = cnt + 1
                    lst.append(str1[i])
                else:
                    lst = []
                    continue
        else:
            if dot_cnt == 3 and cnt <= 3:
                tmp_lst = validate(lst)

                if len(tmp_lst) != 0:
                    fnl_lst.append(tmp_lst)
            lst = []
            cnt = 0
            dot_cnt = 0

    print(fnl_lst)

def main():
    str1 = 'Lorem ipsumle dolor sit amet,52.10.11.33 adipiscing 52.10.11.33.10.4.1consectetur adipiscing elit, nullam sollictudin 192.168.33.2 morbi vitae. aliquam vitae 176.30.10.57'
    ipaddress(str1)

if __name__ == '__main__':
    main()
