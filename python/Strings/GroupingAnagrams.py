def groupanagrams(ary):

    dict={}

    for i in range(0,len(ary)):
        key=''.join(sorted(ary[i]))

        if key in dict:
            dict[key].append(ary[i])
        else:
            dict[key]=[]
            dict[key].append(ary[i])

    for key,val in dict.items():
        print(val)

def main():

    ary=['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

    groupanagrams(ary)

if __name__=='__main__':
    main()
