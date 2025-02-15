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

def FindWordPath_Google(board,word):

    output_lst=[]
    m=0
    n=0
    for i in range(0,len(word)):
        key=word[i]

        if board[m][n]==key:
            output_lst.append('#')
        elif m==0:
            if key > board[m][n]  and n < len(board[0])-1:
                if key < board[m][n+1]:
                    n=n+1
                    output_lst.append('r')
                else:
                    m = m + 1
                    output_lst.append('d')
            elif key > board[m][n]:
                m=m+1
                output_lst.append('d')
            elif key < board[m][n] and n>0:
                n=n-1
                output_lst.append('l')
        elif m > 0:
            if key > board[m][n] and n < len(board[0]) - 1:
                if key < board[m][n + 1]:
                    n = n + 1
                    output_lst.append('r')
                elif m< len(board):
                    if board[m+1][n] is not None:
                        m = m + 1
                        output_lst.append('d')
                    else:
                        n=n+1
                        output_lst.append('r')
            elif key < board[m][n]:
                if key >= board[m][0]:
                    n=n-1
                    output_lst.append('l')
            elif key >=board[m-1][n]:
                m=m-1
                output_lst.append('u')







def main():
    board =[
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y'],
        ['Z', None, None, None, None]
    ]
    word='PM'
    print(board[0])
    print(FindWordPath_Google(board,word))

if __name__=='__main__':
    main()