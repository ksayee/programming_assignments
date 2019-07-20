'''
1125. Smallest Sufficient Team
Hard
In a project, you have a list of required skills req_skills, and a list of people.
The i-th person people[i] contains a list of skills that person has.
Consider a sufficient team: a set of people such that for every required skill in req_skills,
there is at least one person in the team who has that skill.
We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person.
You may return the answer in any order.  It is guaranteed an answer exists.
Example 1:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
'''



import collections
def Validate(tmp,req_skills):

    chk_lst=[]
    for l in tmp:
        chk_lst.extend(l)
    if sorted(set(chk_lst))==sorted(req_skills):
        return True
    else:
        return False

def Combinations_recur(lst,cnt,tmp,fnl_lst,req_skills):

    if len(tmp)>0:
        flg=Validate(tmp,req_skills)
        if flg==True:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,req_skills)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode1125(req_skills, people):

    lst=people
    cnt=[]
    for l in people:
        cnt.append(1)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,req_skills)
    sort_list=sorted(fnl_lst,key=lambda x:len(x))
    return sort_list[0]

def main():

    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    print(LeetCode1125(req_skills,people))

    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    print(LeetCode1125(req_skills, people))

if __name__=='__main__':
    main()