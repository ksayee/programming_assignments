
def lastword(str1):

    cnt=0
    found=False
    for i in range(len(str1)-1,-1,-1):
        if str1[i]==' ' and found==False:
            continue
        elif str1[i]==' ':
            break
        else:
            cnt=cnt+1
            found=True

    return cnt

def main():
    str1='The sky is very blue   '
    print('Length of last word is:',lastword(str1))

    str1 = 'The sky is very blue'
    print('Length of last word is:', lastword(str1))


if __name__=='__main__':
    main()
