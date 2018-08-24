def StringRotations(str1,str2):

    for i in range(0,len(str1)):

        tmp=str1[i:]+str1[0:i]
        if tmp==str2:
            return True

    return False

def main():

    str1 = 'ABACD'
    str2 = 'CDABA'
    print(StringRotations(str1,str2))

    str1 = 'GEEKS'
    str2 = 'EKSGE'
    print(StringRotations(str1,str2))

if __name__=='__main__':
    main()