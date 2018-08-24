def AllRotations(str1):

    for i in range(0,len(str1)):
        print(str1[i:]+str1[0:i])

def main():

    str1 = 'geeks'
    AllRotations(str1)

    str1 = 'abc'
    AllRotations(str1)

if __name__=='__main__':
    main()