'''
Problem Description
Write a function to crush candy in a one dimensional board.
In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many times as possible.
Sample inputs - Expected outputs
ABBBCC -> ACC
ABCCCBB -> A
'''

def Compression(candy):
    tmp=[]
    prev=candy[0]
    cnt=1
    for i in range(1,len(candy)):
        curr=candy[i]
        if prev!=curr:
            if cnt<3:
                tmp.append(prev)
                tmp.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    if cnt<3:
        tmp.append(prev)
        tmp.append(str(cnt))
    return ''.join(tmp)

def Expansion(compress):

    tmp=[]
    prev=compress[0]
    for i in range(1,len(compress)):
        key=compress[i]
        try:
            num=int(key)
            j=0
            while j<num:
                tmp.append(prev)
                j=j+1
        except:
            prev=key
    return ''.join(tmp)

def CandyCrushBloomberg(candy):

    prev=''
    while True:
        compress=Compression(candy)
        if len(compress)==0:
            return ''
        candy=Expansion(compress)
        if prev==candy:
            break
        prev=candy
    return candy

def main():

    candy='ABBBCC'
    print(CandyCrushBloomberg(candy))

    candy = 'ABCCCBB'
    print(CandyCrushBloomberg(candy))

    candy = 'AABCCCDDDDDBBA'
    print(CandyCrushBloomberg(candy))

    candy = 'AABBBACCDDDDC'
    print(CandyCrushBloomberg(candy))

if __name__=='__main__':
    main()