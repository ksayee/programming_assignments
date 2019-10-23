'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations.
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
For example, in this diagram, 6 and 8 have a common ancestor of 4.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11


parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.
Sample input and output:
hasCommonAncestor(parentChildPairs1, 3, 8) => false
hasCommonAncestor(parentChildPairs1, 5, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 9) => true
hasCommonAncestor(parentChildPairs1, 1, 3) => false
hasCommonAncestor(parentChildPairs1, 7, 11) => true
hasCommonAncestor(parentChildPairs1, 6, 5) => true
hasCommonAncestor(parentChildPairs1, 5, 6) => true
Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]
hasCommonAncestor(parentChildPairs2, 4, 12) => true
hasCommonAncestor(parentChildPairs2, 1, 6) => false
hasCommonAncestor(parentChildPairs2, 1, 12) => false
'''

def findParent_recur(dict,fnl_dict,key,lst):

    for item in lst:
        if item in dict.keys():
            fnl_dict[key].extend(dict[item])
            findParent_recur(dict, fnl_dict, key, dict[item])
    return

def Indeed(parentChildPairs,num1,num2):

    dict={}
    for tup in parentChildPairs:
        parent=tup[0]
        child=tup[1]
        if child in dict.keys():
            dict[child].append(parent)
        else:
            dict[child]=[]
            dict[child].append(parent)

    fnl_dict={}

    for key,val in dict.items():
        fnl_dict[key]=[]
        fnl_dict[key].extend(val)

        for v in val:
            if v in dict.keys():
                fnl_dict[key].extend(dict[v])
                findParent_recur(dict,fnl_dict,key,dict[v])

    if num1 not in fnl_dict.keys() or num2 not in fnl_dict.keys():
        return False
    else:
        if len(set(fnl_dict[num1]) & set(fnl_dict[num2]))>0:
            return True
        else:
            return False

def main():

    print("First Input")
    parentChildPairs = [
        (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
        (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
    ]
    print(Indeed(parentChildPairs,3, 8))
    print(Indeed(parentChildPairs, 5, 8))
    print(Indeed(parentChildPairs, 6, 8))
    print(Indeed(parentChildPairs, 6, 9))
    print(Indeed(parentChildPairs, 1, 3))
    print(Indeed(parentChildPairs, 7, 11))
    print(Indeed(parentChildPairs, 6, 5))
    print(Indeed(parentChildPairs, 5, 6))

    print("Second Input")
    parentChildPairs = [
        (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
        (2, 3), (3, 4), (5, 6), (5, 7), (7, 8)
    ]
    print(Indeed(parentChildPairs, 4, 12))
    print(Indeed(parentChildPairs, 1, 6))
    print(Indeed(parentChildPairs, 1, 12))

if __name__=='__main__':
    main()