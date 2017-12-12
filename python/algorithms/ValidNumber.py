
def validnumber(str1):

    dec_flg=0
    for i in range(0,len(str1)):
        if ord(str1[i])>=48 and ord(str1[i])<=57:
            continue
        elif str1[i]=='.' and dec_flg==0:
            dec_flg=1
        elif ord(str1[i])<48 or ord(str1[i])>57:
            return False
        elif str1[i]=='.' and dec_flg==1:
            return False
    return True

def main():
    str1='123'
    print('Is this a valid number?',validnumber(str1))

    str1 = '0.1'
    print('Is this a valid number?', validnumber(str1))

    str1 = 'abc'
    print('Is this a valid number?', validnumber(str1))

    str1 = '0.12.1'
    print('Is this a valid number?', validnumber(str1))

    str1 = '0.12ab'
    print('Is this a valid number?', validnumber(str1))

if __name__=='__main__':
    main()