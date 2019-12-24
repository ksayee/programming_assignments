'''
Program to check for a Valid IMEI Number
International Mobile Equipment Identity (IMEI) is a number, usually unique, to identify mobile phones, as well as some satellite phones.
It is usually found printed inside the battery compartment of the phone, but can also be displayed on-screen on most phones by entering *#06# on the
dialpad, or alongside other system information in the settings menu on smartphone operating systems.
The IMEI number is used by a GSM network to identify valid devices and therefore can be used for stopping a stolen phone from accessing that network.
Source: Wikipedia
The IMEI (15 decimal digits: 14 digits plus a check digit) includes information on the origin, model, and serial number of the device.
The IMEI is validated in following steps:
Starting from the rightmost digit, double the value of every second digit (e.g., 7 becomes 14).
If doubling of a number results in a two digits number i.e greater than 9(e.g., 7 × 2 = 14), then add the digits of
the product (e.g., 14: 1 + 4 = 5), to get a single digit number.
Now take the sum of all the digits.
Check if the sum is divisible by 10 i.e.(total modulo 10 is equal to 0) then the IMEI number is valid; else it is not valid.
Example:
Input IMEI : 490154203237518
Output : Since, 60 is divisible by 10, hence the given IMEI number is Valid.
'''

def ValidIMEINumber(num):

    IMEI=str(num)
    if len(IMEI)!=15:
        return False
    sum=0
    for i in range(0,len(IMEI)):
        key=IMEI[i]
        if i%2!=0:
            double=int(key)*2
            while double!=0:
                rem=double%10
                sum=sum+rem
                double=double//10
        else:
            sum=sum+int(key)
    if sum%60==0:
        return True
    else:
        return False

def main():

    num=490154203237518
    print(ValidIMEINumber(num))

if __name__=='__main__':
    main()