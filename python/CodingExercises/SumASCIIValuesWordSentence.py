'''
Sums of ASCII values of each word in a sentence
We are given a sentence of english language(can also contain digits), we need to compute and print the sum of ASCII values of characters of each word in that sentence.
Examples:
Input :  GeeksforGeeks, a computer science portal for geeks
Output : Sentence representation as sum of ASCII each character in a word:
         1361 97 879 730 658 327 527
         Total sum -> 4579
Here, [GeeksforGeeks, ] -> 1361, [a] -> 97, [computer] -> 879, [science] -> 730
      [portal] -> 658, [for] -> 327, [geeks] -> 527
Input : I am a geek
Output : Sum of ASCII values:
         73 206 97 412
         Total sum -> 788
'''

def SumASCIIValuesWordSentence(str1):

    sum=0
    for i in range(0,len(str1)):
        key=str1[i]
        if key==' ':
            pass
        else:
            sum=sum+ord(key)
    return sum

def main():

    str1='GeeksforGeeks, a computer science portal for geeks'
    print(SumASCIIValuesWordSentence(str1))

    str1 = 'I am a geek'
    print(SumASCIIValuesWordSentence(str1))

if __name__=='__main__':
    main()