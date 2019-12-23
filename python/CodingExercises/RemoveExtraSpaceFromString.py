'''
Remove extra spaces from a string
Given a string containing many consecutive spaces, trim all spaces so that all words should contain only a single space between them.
The conversion should be done in-place and solution should handle trailing and
leading spaces and also remove preceding spaces before common punctuation like full stop, comma and a question mark.
Examples:

Input:
str = "   Hello Geeks . Welcome   to  GeeksforGeeks   .    ";
Output:
"Hello Geeks. Welcome to GeeksforGeeks."

Input:
str = "GeeksforGeeks";
Output:
"GeeksforGeeks"
(No change is needed)
'''

def RemoveExtraSpaceFromString(str1):

    lst=str1.split(' ')
    output_list=[]

    for word in lst:

        if len(word)==1:
            if word>='A'and word<='Z' or word>='a'and word<='z':
                output_list.append(' ')
                output_list.append(word)
            else:
                output_list.append(word)
        elif len(word)>1:
            if len(output_list)==0:
                output_list.append(word)
            else:
                output_list.append(' ')
                output_list.append(word)
        else:
            pass
    return ''.join(output_list)

def main():
    
    str1="   Hello Geeks . Welcome   to  GeeksforGeeks   .    "
    print(RemoveExtraSpaceFromString(str1))

    str1 = "GeeksforGeeks"
    print(RemoveExtraSpaceFromString(str1))

if __name__=='__main__':
    main()