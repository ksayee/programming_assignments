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

def findancestors(num, ancestors_lst,child_parent_dict):

    if num in child_parent_dict.keys():
        ancestors_lst.extend(child_parent_dict[num])
        for item in child_parent_dict[num]:
            ancestors_lst = findancestors(item, ancestors_lst, child_parent_dict)
    return ancestors_lst

def hasCommonAncestor(parentChildPairs1, num1, num2):

    child_parent_dict={}
    for tup in parentChildPairs1:
        child = tup[1]
        parent = tup[0]
        if child not in child_parent_dict.keys():
            child_parent_dict[child]=[]
            child_parent_dict[child].append(parent)
        else:
            child_parent_dict[child].append(parent)

    num1_ancestors=[]
    num2_ancestors=[]

    num1_ancestors = findancestors(num1,[],child_parent_dict)
    num2_ancestors =findancestors(num2,[],child_parent_dict)
    print(num1_ancestors,num2_ancestors)

    if len(list(set(num1_ancestors) & set(num2_ancestors))) >= 1:
        return True
    else:
        return False

def main():

    parentChildPairs1 = [
        (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
        (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
    ]
    print(hasCommonAncestor(parentChildPairs1, 3, 8)) #false
    print(hasCommonAncestor(parentChildPairs1, 5, 8)) # true
    print(hasCommonAncestor(parentChildPairs1, 6, 8)) # true
    print(hasCommonAncestor(parentChildPairs1, 6, 9)) # true
    print(hasCommonAncestor(parentChildPairs1, 1, 3)) # false
    print(hasCommonAncestor(parentChildPairs1, 7, 11)) # true
    print(hasCommonAncestor(parentChildPairs1, 6, 5)) # true
    print(hasCommonAncestor(parentChildPairs1, 5, 6)) #true

    parentChildPairs2 = [
        (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
        (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
    ]
    print(hasCommonAncestor(parentChildPairs2, 4, 12)) # true
    print(hasCommonAncestor(parentChildPairs2, 1, 6)) # false
    print(hasCommonAncestor(parentChildPairs2, 1, 12)) # false

if __name__=='__main__':
    main()