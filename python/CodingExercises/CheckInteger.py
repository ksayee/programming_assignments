# Program to check if input is an integer or a string
# Write a function to check whether a given input is an integer or a string.

def CheckInteger(str1):

    print("Input Data:",str1)

    try:
        tmp=int(str1)
        return "Integer"
    except:
        return "String"

def main():

    str1='127'
    print(CheckInteger(str1))

    str1 = '199.7'
    print(CheckInteger(str1))

    str1 = '122B'
    print(CheckInteger(str1))

if __name__=='__main__':
    main()