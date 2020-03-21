'''
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
'''

def LeetCode1291(low,high):

    output_lst=[]
    while low<=high:
        num=low
        if len(str(num))!=len(set(str(num))):
            pass
        else:
            tmp=[]
            flg=True
            while num!=0:
                rem=num%10
                tmp.append(rem)
                num=num//10
            tmp.reverse()
            for i in range(1,len(tmp)):
                if tmp[i]-1!=tmp[i-1]:
                    flg=False
                    break
            if flg==True:
                output_lst.append(low)
        low=low+1
    return output_lst

def main():

    low=100
    high=300
    print(LeetCode1291(low,high))

    low = 1000
    high = 13000
    print(LeetCode1291(low, high))

if __name__=='__main__':
    main()