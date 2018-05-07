'''
500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: [Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''


def findWords(words):
    lst1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    lst2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    lst3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    fnl = []
    tmp_lst = []

    for word in words:
        flg = True
        for i in range(0, len(word)):
            key = word[i].lower()
            if i == 0:
                if key in lst1:
                    tmp_lst = lst1
                elif key in lst2:
                    tmp_lst = lst2
                elif key in lst3:
                    tmp_lst = lst3
            else:
                if key not in tmp_lst:
                    flg = False
                    break

        if flg == True:
            fnl.append(word)
    return fnl

def main():
    words=["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(words))

if __name__=='__main__':
    main()