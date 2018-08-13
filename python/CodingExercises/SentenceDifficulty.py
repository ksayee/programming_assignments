# Calculate the difficulty of a sentence
# Calculate difficulty of a given sentence. Here a Word is considered hard if it has 4 consecutive consonants or number of consonants are more than number of vowels. Else word is easy. Difficulty of sentence is defined as 5*(number of hard words) + 3*(number of easy words).

def ConsonantsVovels(vol,word):

    lst=list(word)
    con_cnt=0
    vol_cnt=0
    max_con_cnt=-99
    cnt=0
    flg=False
    for l in lst:
        if l in vol:
            vol_cnt=vol_cnt+1
            if flg==True:
                if cnt > max_con_cnt:
                    max_con_cnt = cnt
            flg = False
        else:
            if flg==True:
                cnt=cnt+1
            else:
                cnt=1
                flg=True
            con_cnt=con_cnt+1
    if cnt>max_con_cnt:
        max_con_cnt=cnt
    fnl_lst=[]
    fnl_lst.append(con_cnt)
    fnl_lst.append(vol_cnt)
    fnl_lst.append(cnt)
    return fnl_lst

def SentenceDifficulty(str):

    vol=['a','e','i','o','u']
    lst=str.lower().split()

    hard_word=0
    easy_word=0
    for word in lst:
        fnl_lst=ConsonantsVovels(vol,word)
        if fnl_lst[2]>=4 or (fnl_lst[0]>fnl_lst[1]):
            hard_word=hard_word+1
        else:
            easy_word=easy_word+1

    return 5*hard_word+3*easy_word

def main():

    str="Difficulty of sentence"
    print(SentenceDifficulty(str))

    str = "I am a geek"
    print(SentenceDifficulty(str))

    str = "We are geeks"
    print(SentenceDifficulty(str))


if __name__=='__main__':
    main()