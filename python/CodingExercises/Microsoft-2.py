# There are given n machiines and a list of successes, return the max number of loggest successes from the list.

def Solution(machines,input_ary):

    tot_success=0
    max_success=0

    for item in input_ary:

        i = 0
        flg = True
        while i<machines:
            if item[i] == 'Y':
                pass
            elif item[i] == 'N':
                flg = False
                break
            i = i+1

        if i == machines and flg == True:
            tot_success = tot_success + 1
        else:
            if tot_success > max_success:
                max_success = tot_success
                tot_success = 0
            else:
                tot_success = 0

    if tot_success > max_success:
        max_success = tot_success

    return max_success
    
def main():
    
    machines= 3
    input_ary = ['YYY','YNY','NNN','NNY','YYN','YYY','YYY','NNN','NNN','YYY','YYY','YYY''YYY','YYY']
    print(Solution(machines,input_ary))

if __name__=='__main__':
    main()