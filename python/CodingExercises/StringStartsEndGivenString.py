'''
Find if a string starts and ends with another given string
Given a string str and a corner string cs, we need to find out whether the string str starts and ends with the corner string cs or not.
Examples:
Input : str = "geeksmanishgeeks", cs = "geeks"
Output : Yes
Input : str = "shreya dhatwalia", cs = "abc"
Output : No
'''

def StringStartsEndGivenString(str1, pattern):

    try:
        idx=str1.index(pattern)
        if idx==0:
            str1=str1[-len(pattern):]
            if pattern==str1:
                return True
            else:
                return False
    except:
        return False
def main():

    str1='geeksmanishgeeks'
    pattern='geeks'
    print(StringStartsEndGivenString(str1,pattern))

    str1 = 'shreya dhatwalia'
    pattern = 'abc'
    print(StringStartsEndGivenString(str1, pattern))

if __name__=='__main__':
    main()