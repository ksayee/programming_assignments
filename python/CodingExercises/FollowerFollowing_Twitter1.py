'''
Given a table with two columns, follower and following, find a list of mutual follows.
A mutual follow is defined as: If 1 follows 2, and 2 follows 1, it is a mutual follow. To simplify, we do not consider transitive dependencies.

Input:
Follower, Following
1,2
2,3
1,3
4,3
3,4
3,2
5,8
4,8
6,4
7,5
8,5

Output:
2,3
3,4
5,8
'''

def solution1(lst):

    dict={}
    output=[]

    for item in lst:
        if item[1] in dict.keys():
            if item[0] in dict[item[1]]:
                tmp=[]
                tmp.append(item[0])
                tmp.append(item[1])
                output.append(tmp.copy())

        key=item[0]
        if key in dict.keys():
            dict[key].append(item[1])
        else:
            dict[key]=[]
            dict[key].append(item[1])
    return output

def main():
    
    lst=[[1,2],[2,3],[1,3],[4,3],[3,4],[3,2],[5,8],[4,8],[6,4],[7,5],[8,5]]
    print(solution1(lst))

if __name__=='__main__':
    main()