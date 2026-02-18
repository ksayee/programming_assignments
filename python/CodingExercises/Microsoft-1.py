# Given any array with element, please return the number which is occuring many times and also give the maximum number if there is a tie

def Solution(ary):

    output_dict={}

    for item in ary:
        if item not in output_dict.keys():
            output_dict[item]=1
        else:
            output_dict[item]+=1

    return sorted(output_dict.items(), key=lambda x: (-x[1],-x[0]))[0][0]
    
def main():
    
    ary=[1,1,2,2,3,3,4,5,6]
    print(Solution(ary))

if __name__=='__main__':
    main()