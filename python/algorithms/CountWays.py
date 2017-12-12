
def countways(num):

    f=[0]*1000

    f[0]=1
    f[1]=2

    for i in range(2,num):
        f[i]=f[i-1]+f[i-2]

    print('Number of ways to Climb Stairs:',f[num-1])


def main():

    n=5
    countways(n)

if __name__=='__main__':
    main()
