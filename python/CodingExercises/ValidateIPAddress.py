'''
Validate if a string is a valid IP address.
'''

def ValidateIPAddress(ip):

    lst=ip.split('.')

    if len(lst)!=4:
        return False

    flg=True
    for i in range(0,len(lst)):

        try:
            key=int(lst[i])
            if key>=0 and key<=255:
                continue
            else:
                flg=False
                break
        except:
            flg=False
            break
    return flg

def main():

    ip = '69.89.18.226'
    print(ValidateIPAddress(ip))

    ip='69.89.345.226'
    print(ValidateIPAddress(ip))

    ip = '69.89.345'
    print(ValidateIPAddress(ip))

    ip = '69.89.345.aa'
    print(ValidateIPAddress(ip))

if __name__=='__main__':
    main()