# Given two array that are sorted, merge both the arrays into one and don't remove any duplicates

def Solution(input_ary1,input_ary2):

    i = 0
    j = 0

    output_ary = []

    while True:
        if i <len(input_ary1) and j <len(input_ary2):
            if input_ary1[i] < input_ary2[j]:
                output_ary.append(input_ary1[i])
                i = i + 1
            elif input_ary2[j] < input_ary1[i]:
                output_ary.append(input_ary2[j])
                j = j + 1
            elif input_ary1[i] == input_ary2[j]:
                output_ary.append(input_ary1[i])
                output_ary.append(input_ary2[j])
                i = i + 1
                j = j + 1
        elif i == len(input_ary1) and j <len(input_ary2):
            output_ary.extend(input_ary2[j:])
            j = len(input_ary2)
        elif j == len(input_ary2) and i <len(input_ary1):
            output_ary.extend(input_ary1[i:])
            i = len(input_ary1)
        elif i == len(input_ary1) and j == len(input_ary2):
            break

    return output_ary

def main():
    
    input_ary1 = [1,1,2,4,6,7,7,8,14,17]
    input_ary2 = [1,2,5,5,8,9,11]
    print(Solution(input_ary1,input_ary2))

if __name__=='__main__':
    main()