'''
Given a word_list array, group all the anagrams together
'''

def groupanagrams(word_list):

    lst={}

    for word in word_list:

        key=''.join(sorted(word))

        if key in lst.keys():
            lst[key].append(word)
        else:
            tmp=[]
            tmp.append(word)
            lst[key]=tmp

    return lst

def main():
    
    word_list=["cat", "dog", "tac", "god", "act", "gdo"]
    print(groupanagrams(word_list))

if __name__=='__main__':
    main()