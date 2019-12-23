'''
Print the string by ignoring alternate occurrences of any character
Given a string of both uppercase and lowercase alphabets, the task is
to print the string with alternate occurrences of any character dropped(including space and consider upper and lowercase as same).
Examples:
Input : It is a long day Dear.
Output : It sa longdy ear.
Print first I and then ignore next i.
Similarly print first space then
ignore next space.
Input : Geeks for geeks
Output : Geks fore
'''

import collections
def PrintStringIgnoringAlternateOccurencesCharacter(str1):

    output_list=[]
    dict={}

    for i in range(0,len(str1)):
        key=str1[i].lower()
        if key in dict.keys():
            del dict[key]
        else:
            output_list.append(str1[i])
            dict[key]=1

    return ''.join(output_list)

def main():
    
    str1="It is a long day Dear."
    print(PrintStringIgnoringAlternateOccurencesCharacter(str1))

    str1 = "Geeks for geeks"
    print(PrintStringIgnoringAlternateOccurencesCharacter(str1))

if __name__=='__main__':
    main()