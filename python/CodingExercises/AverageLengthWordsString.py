'''
Find the Average length of the word in the string.
'''

def AverageLenghtWordsString(str1):

    lst=str1.split()

    word_cnt=0

    for i in range(0,len(lst)):
        key=lst[i]
        word_cnt=word_cnt+len(key)

    return word_cnt/len(lst)

def main():

    str1='The sky is very blue today'
    print(AverageLenghtWordsString(str1))

    str1 = 'This is Kartik Sayee working in Expedia'
    print(AverageLenghtWordsString(str1))

    str1 = 'United States'
    print(AverageLenghtWordsString(str1))

if __name__=='__main__':
    main()