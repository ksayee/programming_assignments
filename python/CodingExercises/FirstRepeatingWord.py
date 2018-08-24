# Find the first repeated word in a string
# Given a string, Find the 1st repeated word in a string

def FirstRepeatingWord(str):

    lst=str.split()

    for i in range(0,len(lst)):
        key=lst[i]
        if key in lst[i+1:]:
            return key

    return "No repeating Word"

def main():

    str='Ravi had been saying that he had been there'
    print(FirstRepeatingWord(str))

    str = 'Ravi had been saying that'
    print(FirstRepeatingWord(str))

    str = 'he had had he'
    print(FirstRepeatingWord(str))

if __name__=='__main__':
    main()