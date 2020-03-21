'''
212. Word Search II
Given a 2D board and a list of words from the dictionary, find all words in the board.
 must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''

def dfs(newboard,word,i,j,k):

    if i<0 or j<0 or i>=len(newboard)or j>=len(newboard[0]):
        return False
    if newboard[i][j]==word[k]:
        if k==len(word)-1:
            return True
        tmp=newboard[i][j]
        newboard[i][j]='#'
        if dfs(newboard,word,i+1,j,k+1) or dfs(newboard,word,i-1,j,k+1) or dfs(newboard,word,i,j+1,k+1) or dfs(newboard,word,i,j-1,k+1):
            return True
        newboard[i][j]=tmp
    return False

def LeetCode212(board,words):

    output_lst=[]
    for word in words:
        newboard=[]
        for lst in board:
            newboard.append(lst.copy())
        flg=False
        for i in range(0,len(newboard)):
            for j in range(0,len(newboard[0])):
                if dfs(newboard,word,i,j,0):
                    flg=True
        if flg==True:
            output_lst.append(word)
    return output_lst

def main():
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(LeetCode212(board,words))

if __name__=='__main__':
    main()