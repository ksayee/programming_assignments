def fibonaci():

    fib=[0]*100

    fib[0]=0
    fib[1]=1

    for i in range(2,100):
        fib[i]=fib[i-1]+fib[i-2]

    print(fib)

def main():

    fibonaci()

if __name__=='__main__':
    main()
