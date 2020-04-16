'''
Run length encoding of string. See below for example:
aaaaabbbccd => a5b3c2d1
xyz => x1y1z1
'''

def RunEncodingLength(str1):

    lst=list(str1)
    prev=lst[0]
    cnt=1
    output_lst=[]
    for i in range(1,len(lst)):
        curr=lst[i]
        if prev!=curr:
            output_lst.append(prev)
            output_lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    output_lst.append(prev)
    output_lst.append(str(cnt))
    return ''.join(output_lst)

def main():

    str1='aaaaabbbccd'
    print(RunEncodingLength(str1))

    str1 = 'xyz'
    print(RunEncodingLength(str1))

if __name__=='__main__':
    main()