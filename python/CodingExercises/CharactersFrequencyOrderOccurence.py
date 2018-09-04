# Print characters and their frequencies in order of occurrence
# Given a string str containing only lowercase characters.
# The problem is to print the characters along with their frequency in order of their occurrence and in the given format explained in the examples below.

import collections
def CharactersFrequencyOrderOccurence(str1):

    lst=list(str1)

    dict=collections.Counter(str1)

    tmp=[]
    fnl_lst=[]
    for i in range(0,len(lst)):

        key=lst[i]

        if key not in tmp:
            val=dict[key]

            fnl_lst.append(key+str(val))
            tmp.append(key)

    return ''.join(fnl_lst)

def main():

    str1='geeksforgeeks'
    print(CharactersFrequencyOrderOccurence(str1))

    str1 = 'elephant'
    print(CharactersFrequencyOrderOccurence(str1))


if __name__=='__main__':
    main()