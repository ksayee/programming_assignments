'''
1086.High Five
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
Note:
1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
'''

def LeetCode1086(ary):

    students=[]
    dict={}
    for lst in ary:
        student_id=lst[0]
        student_score=lst[1]
        if student_id in dict.keys():
            dict[student_id].append(student_score)
        else:
            dict[student_id]=[]
            dict[student_id].append(student_score)

    for key,val in dict.items():
        sum=0
        if len(val)>5:
            val.sort()
            while len(val)!=5:
                val.pop(0)
        for v in val:
            sum=sum+v
        avg=int(sum/len(val))
        tmp=[]
        tmp.append(key)
        tmp.append(avg)
        students.append(tmp)
    return students

def main():

    ary=[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    print(LeetCode1086(ary))

if __name__=='__main__':
    main()