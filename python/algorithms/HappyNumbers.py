import math

def happynumbers(n):

    lst=[]
    for i in range(1,n+1):
        c_num=i
        flg=True
        while flg==True:
            tmp=c_num
            sum=0
            while tmp!=0:
                sum=sum+math.pow(tmp%10,2)
                tmp=int(tmp/10)
            c_num=sum
            if c_num<10:
                flg=False
        if c_num==1:
            lst.append(i)
    print(len(lst))

def main():
    n=1000
    happynumbers(n)

if __name__=='__main__':
    main()
