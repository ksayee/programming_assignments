# Please write a function to count the number of words in the following sentence.
# The output should display the words with higher counts first.
# Words with the same count should appear arranged alphabetically.
# Input = ‘the quick brown fox jumps over the car car’
# Output:
# car – 2
# the – 2
# brown – 1
# fox – 1
# jumps – 1
# over – 1
# quick – 1

def SentenceWordCount(str1):
    lst=str1.split()
    dict={}
    for word in lst:
        if word in dict.keys():
            dict[word]=dict.get(word)+1
        else:
            dict[word]=1
    return sorted(dict.items(),key=lambda x:x[1],reverse=True)

def main():

    str1='the quick brown fox jumps over the car car'
    print(SentenceWordCount(str1))

if __name__=='__main__':
    main()