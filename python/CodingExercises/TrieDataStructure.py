'''
Program to generate all possible valid IP addresses from given string
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
Examples :
Input : 25525511135
Output : [“255.255.11.135”, “255.255.111.35”]
Explanation:
These are the only valid possible
IP addresses.
Input : "25505011535"
Output : []
Explanation :
We cannot generate a valid IP
address with this string.
'''

class TrieNode(object):
    def __init__(self):
        self.dict={}
        self.endOfWord=False

class TrieStructure(object):
    def __init__(self,value):
        self.root=TrieNode()

    def addWord(self,word):

        current=self.root
        letters=list(word)
        for i in range(0,len(letters)):
            letter=letters[i]
            while True:
                if letter in current.dict.keys():
                    node=current.dict[letter]
                    current=node
                else:
                    node=TrieNode()
                    current.dict[letter]=node
                    break
            current=node
            if i==len(letters)-1:
                current.endOfWord=True



        return

def main():

    obj=TrieStructure()
    lst=["the", "a", "there", "answer", "any", "by","bye", "their"]
    for word in lst:
        obj.addWord(word)


if __name__=='__main__':
    main()