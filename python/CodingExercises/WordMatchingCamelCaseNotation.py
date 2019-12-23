'''
Print all words matching a pattern in CamelCase Notation Dictonary
Given a dictionary of words where each word follows CamelCase notation,
print all words in the dictionary that match with a given pattern consisting of uppercase characters only.

CamelCase is the practice of writing compound words or phrases such that each word or abbreviation begins with a
capital letter. Common examples include: “PowerPoint” and “WikiPedia”, “GeeksForGeeks”, “CodeBlocks”, etc.

Examples:
Input:
dict[] = ["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek",
"HiTechWorld", "HiTechCity", "HiTechLab"]

For pattern "HT",
Output: ["HiTech", "HiTechWorld", "HiTechCity", "HiTechLab"]

For pattern "H",
Output: ["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek",
    "HiTechWorld", "HiTechCity", "HiTechLab"]

For pattern "HTC",
Output: ["HiTechCity"]


Input:
dict[] = ["WelcomeGeek","WelcomeToGeeksForGeeks", "GeeksForGeeks"]

For pattern "WTG",
Output: ["WelcomeToGeeksForGeeks"]

For pattern "GFG",
Output: [GeeksForGeeks]

For pattern "GG",
Output: No match found
'''

def WordMatchingCamelCaseNotation(ary,pattern):

    output_list=[]

    for word in ary:
        flg=True
        tmp_word=word
        for letter in pattern:
            try:
                idx=word.index(letter)
                word=word[idx+1:]
            except:
                flg=False
        if flg==True:
            output_list.append(tmp_word)
    return output_list


def main():
    
    ary=["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek","HiTechWorld", "HiTechCity", "HiTechLab"]
    pattern="HT"
    print(WordMatchingCamelCaseNotation(ary,pattern))

    pattern = "H"
    print(WordMatchingCamelCaseNotation(ary, pattern))

    pattern = "HTC"
    print(WordMatchingCamelCaseNotation(ary, pattern))

    ary = ["WelcomeGeek","WelcomeToGeeksForGeeks", "GeeksForGeeks"]
    pattern = "WTG"
    print(WordMatchingCamelCaseNotation(ary, pattern))

    pattern = "GFG"
    print(WordMatchingCamelCaseNotation(ary, pattern))

    pattern = "GG"
    print(WordMatchingCamelCaseNotation(ary, pattern))

if __name__=='__main__':
    main()