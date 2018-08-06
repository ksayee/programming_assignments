# Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.
def Pangram(str1):

    print("Sentence:",str1)
    a=[0]*26
    flg=True
    for i in range(0,len(str1)):
        if str1[i]!=' ':
            key=str1[i].upper()
            a[ord(key)-65]=1

    for i in range(0,len(a)):
        if a[i]==0:
            flg=False
    return flg

def main():

    str1='The quick brown fox jumps over the lazy dog'
    print(Pangram(str1))

    str1 = 'The quick brown fox jumps over the dog'
    print(Pangram(str1))


if __name__=='__main__':
    main()