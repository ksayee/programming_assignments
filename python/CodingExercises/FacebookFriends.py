# Find number of Friends of Each person

def FacebookFriends(ary):

    dict={}

    for lst in ary:
        for l in lst:
            if l in dict.keys():
                dict[l]=dict.get(l)+(len(lst))-1
            else:
                dict[l]=len(lst)-1

    return dict

def main():

    ary = [['A', 'B', 'C'], ['B', 'F', 'D'], ['A', 'D'], ['E']]
    print(FacebookFriends(ary))

    ary = [['A'], ['B'], ['D'], ['C'],['E']]
    print(FacebookFriends(ary))

if __name__=='__main__':
    main()