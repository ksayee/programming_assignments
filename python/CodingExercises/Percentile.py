'''
ary = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
n = 0.9
'''

def Percentile(ary,n):

    ary.sort()
    lgt=len(ary)
    for i in range(0,len(ary)):
        if (i+1)/lgt<0.9:
            pass
        else:
            break
    return ary[i]

def main():
    ary = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    n=0.9
    print(Percentile(ary,n))
    
if __name__=='__main__':
    main()