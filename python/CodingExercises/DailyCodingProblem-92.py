'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.
We're given a hashmap with a key courseId and value a list of courseIds,
which represents that the prerequsite of courseId is courseIds. Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.
For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
'''

def GetItem(key,val,dict,fnl_lst):

    if len(val)==0:
        if key not in fnl_lst:
            fnl_lst.append(key)
        return
    else:
        for l in val:
            GetItem(l,dict[l],dict,fnl_lst)
        if key not in fnl_lst:
            fnl_lst.append(key)

def DailyCodingProblem92(dict):

    fnl_lst=[]
    for key,val in dict.items():
        GetItem(key,val,dict,fnl_lst)
    return fnl_lst

def main():

    dict={'CSC400': ['CSC300', 'CSC200'],'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
    print(DailyCodingProblem92(dict))

if __name__=='__main__':
    main()