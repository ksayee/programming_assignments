'''
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
'''

def DailyCodingProblem889(input_str):

    prev=input_str[0]
    cnt=1
    output_lst = []
    for i in range(1,len(input_str)):
        curr = input_str[i]
        if curr!=prev:
            output_lst.append(str(cnt))
            output_lst.append(prev)
            cnt=1
        else:
            cnt = cnt +1
        prev=curr
    output_lst.append(str(cnt))
    output_lst.append(curr)

    return ''.join(output_lst)

def main():

    input_str="AAAABBBCCDAA"
    print(DailyCodingProblem889(input_str))

if __name__=='__main__':
    main()