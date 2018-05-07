'''
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''


def judgeCircle(moves):
    valid = [0, 0]

    for i in range(len(moves)):
        key = moves[i]
        if key == 'U':
            valid[1] = valid[1] + 1
        elif key == 'D':
            valid[1] = valid[1] - 1
        elif key == 'L':
            valid[0] = valid[0] - 1
        elif key == 'R':
            valid[0] = valid[0] + 1

    if valid == [0, 0]:
        return True
    else:
        return False

def main():
    moves="UD"
    print(judgeCircle(moves))

    moves = "LL"
    print(judgeCircle(moves))

if __name__=='__main__':
    main()