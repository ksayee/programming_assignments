'''
Move spaces to front of string in single traversal
Given a string that has set of words and spaces, write a program to move all spaces to front of string, by traversing the string only once.

Examples:

Input  : str = "geeks for geeks"
Output : ste = "  geeksforgeeks"

Input  : str = "move these spaces to beginning"
Output : str = "    movethesespacestobeginning"
There were four space characters in input,
all of them should be shifted in front.
'''

def MoveSpacesFrontString(str1):

    output_list=[]
    lst=str1.split(' ')
    prev_word=''
    for word in lst:
        if len(word)==0:
            output_list.append(' ')
        else:
            if len(prev_word)>0:
                output_list.append(' ')
        prev_word=word

    output_list.append(''.join(lst))
    return ''.join(output_list)

def main():
    
    str1="geeks for geeks"
    print(MoveSpacesFrontString(str1))

    str1 = "move these spaces to beginning"
    print(MoveSpacesFrontString(str1))

    str1 = "move these    spaces   to          beginning"
    print(MoveSpacesFrontString(str1))

if __name__=='__main__':
    main()