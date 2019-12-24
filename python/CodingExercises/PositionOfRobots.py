'''
Position of robot after given movements
Given a robot which can only move in four directions,
UP(U), DOWN(D), LEFT(L), RIGHT(R). Given a string consisting of instructions to move.
Output the coordinates of a robot after executing the instructions. Initial position of robot is at origin(0, 0).
Examples:
Input : move = "UDDLRL"
Output : (-1, -1)
Move U : (0, 0)--(0, 1)
Move D : (0, 1)--(0, 0)
Move D : (0, 0)--(0, -1)
Move L : (0, -1)--(-1, -1)
Move R : (-1, -1)--(0, -1)
Move L : (0, -1)--(-1, -1)
Therefore final position after the complete
movement is: (-1, -1)
Input : move = "UDDLLRUUUDUURUDDUULLDRRRR"
Output : (2, 3)
'''

def PositionOfRobots(move):

    lst=[0,0]

    for i in range(0,len(move)):
        key=move[i]
        if key=='U':
            lst[1]=lst[1]+1
        elif key=='D':
            lst[1]=lst[1]-1
        elif key=='L':
            lst[0]=lst[0]-1
        elif key=='R':
            lst[0]=lst[0]+1
    return lst

def main():

    move='UDDLRL'
    print(PositionOfRobots(move))

    move = 'UDDLLRUUUDUURUDDUULLDRRRR'
    print(PositionOfRobots(move))

if __name__=='__main__':
    main()