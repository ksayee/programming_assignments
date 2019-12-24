'''
Find winner of an election where votes are represented as candidate names
Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate.
Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.

Examples:

Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John',
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.
'''

import collections
def ElectionWinner(ary):

    dict=collections.Counter(ary)

    votes_dict={}
    for key,val in dict.items():
        if val in votes_dict.keys():
            votes_dict[val].append(key)
        else:
            votes_dict[val]=[]
            votes_dict[val].append(key)

    winners=sorted(votes_dict.items(),key=lambda x:x[0],reverse=True)[0][1]
    return sorted(winners)[0]

def main():

    ary=["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]
    print(ElectionWinner(ary))

if __name__=='__main__':
    main()