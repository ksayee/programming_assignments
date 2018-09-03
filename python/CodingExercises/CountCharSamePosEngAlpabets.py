# Count characters at same position as in English alphabet
# Given a string of lower and uppercase characters, the task is to find that how many characters are at same position as in English alphabet.

def CountCharSamePosEngAlpabets(str1):

    cnt=0

    for i in range(0,len(str1)):

        key=str1[i]

        if i==ord(key)-ord('a') or i==ord(key)-ord('A'):
            cnt=cnt+1

    return cnt
def main():

    str1='ABcED'
    print(CountCharSamePosEngAlpabets(str1))

    str1 = 'geeksforgeeks'
    print(CountCharSamePosEngAlpabets(str1))

    str1 = 'alphabetical'
    print(CountCharSamePosEngAlpabets(str1))

if __name__=='__main__':
    main()