# Print the string after the specified character has occurred given no. of times
# Given a string, a character, and a count, the task is to print the string after the specified character has occurred count number of times.Print “Empty string” in case of any unsatisfying conditions.(Given character is not present, or present but less than given count, or given count completes on last index). If given count is 0, then given character doesn’t matter, just print the whole string.

def PrintStringSpecChar(str,chr,cnt):

    tmp_cnt=0
    for i in range(0,len(str)):
        key=str[i]
        if key==chr:
            tmp_cnt=tmp_cnt+1

            if tmp_cnt==cnt:
                return str[i+1:]

def main():

    str='This is demo string'
    chr='i'
    cnt=3
    print(PrintStringSpecChar(str,chr,cnt))

    str = 'geeksforgeeks'
    chr = 'e'
    cnt = 2
    print(PrintStringSpecChar(str, chr, cnt))

if __name__=='__main__':
    main()