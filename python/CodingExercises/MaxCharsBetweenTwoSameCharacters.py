'''
Maximum number of characters between any two same character in a string
Given a string, find the maximum number of characters between any two same character in the string. If no character repeats, print -1.
Examples:

Input : str = "abba"
Output : 2
The maximum number of characters are
between two occurrences of 'a'.

Input : str = "baaabcddc"
Output : 3
The maximum number of characters are
between two occurrences of 'b'.

Input : str = "abc"
Output : -1
'''

def MaxCharsBetweenTwoSameCharacters(str1):

    first_char=str1[0]
    prev_char=''
    curr_char=''
    max_count=-1
    count=0

    for i in range(1,len(str1)):
        curr_char = str1[i]
        if i==1:
            if first_char!=curr_char:
                count=count+1
        else:
            if prev_char==curr_char:
                count=count+1
            elif curr_char==first_char:
                if count>max_count:
                    max_count=count
                count=1
                first_char=prev_char
            else:
                first_char=prev_char
                count=1
        prev_char=curr_char
    return max_count

def main():
    
    str1='abba'
    print(MaxCharsBetweenTwoSameCharacters(str1))

    str1 = 'baaabcddc'
    print(MaxCharsBetweenTwoSameCharacters(str1))

if __name__=='__main__':
    main()