def validnumber(str1):

    dec_flg=False

    for i in range(0,len(str1)):
        key=str1[i]

        if key >='0' and key <='9':
            continue
        elif key=='.':
            if dec_flg==False:
                dec_flg=True
            else:
                return False
        else:
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