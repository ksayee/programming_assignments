'''
79. Word Search
Medium
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

import collections

def dfs(board,word,i,j,k):

    if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
        return False
    if board[i][j]==word[k]:
        tmp=board[i][j]
        board[i][j]='#'
        if k==len(word)-1:
            return True
        elif dfs(board,word,i+1,j,k+1) or dfs(board,word,i-1,j,k+1) or dfs(board,word,i,j+1,k+1) or dfs(board,word,i,j-1,k+1):
            return True
        board[i][j]=tmp
    return False

def LeetCode79(board,word):

    flg=False
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if dfs(board,word,i,j,0):
                flg=True
    return flg

def main():
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word='ABCCED'
    print(LeetCode79(board,word))

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = 'SEE'
    print(LeetCode79(board, word))

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = 'ABCB'
    print(LeetCode79(board, word))
if __name__=='__main__':
    main()