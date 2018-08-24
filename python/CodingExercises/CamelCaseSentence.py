# Camel case of a given sentence
# Given a sentence, task is to remove spaces from the sentence and rewrite in Camel case. It is a style of writing where we don’t have spaces and all words begin with capital letters.

def CamelCaseSentence(str):

    lst=str.split()
    fnl_lst=[]
    for l in lst:

        key=list(l)

        for i in range(0,len(key)):
            s=key[i]
            if i==0:
                fnl_lst.append(s.upper())
            else:
                fnl_lst.append(s)

    return ''.join(fnl_lst)


def main():

    str1='I got intern at geeksforgeeks'
    print(CamelCaseSentence(str1))

    str1 = 'Here comes the garden'
    print(CamelCaseSentence(str1))

if __name__=='__main__':
    main()