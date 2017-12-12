def reversedigit(digit):

    tmp=0
    while digit!=0:
        tmp=(tmp*10)+digit%10
        digit=int(digit/10)
    return tmp

def reversedigit_rec(digit):

    if digit<10:
        print(digit)
    else:
        print(digit%10,end='')
        reversedigit_rec(int(digit/10))

def main():
    digit=345

    print('Reversing Digit: ',reversedigit(digit))
    print('Reversing Using Recurrsion: ',end='')
    reversedigit_rec(digit)

if __name__=='__main__':
    main()
