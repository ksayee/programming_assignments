'''
# "should be 11.5"

2x3 matrix x vec
4, 5, 6
3, 4, 5
-- [val1, val2]
vec  3x1
2
5
6

0x2 + 0x5 + 0x6
'''

class SparseMatrix2D:
    def __init__(self, rows, cols):
        self.mat_dict = {}
        self.rows = rows

        rows_lst=[0] * cols

        self.matrix=[]

        for i in range(0,rows):
            self.matrix.append(rows_lst.copy())


    def set(self, row, col, value):

        tup = (row, col)
        self.mat_dict[tup] = value

        self.matrix[row][col]=value

    def solution1(self, vec):

        result_vec = []

        for i in range(0, len(vec)):
            result=0
            for key, val in self.mat_dict.items():
                if i == key[0]:
                    tup = (i, key[1])
                    if tup in self.mat_dict.keys():
                        result = result+ (vec[i] * self.mat_dict[tup])
            result_vec.append(result)
        return result_vec

    def solution2(self, vec):

        result_vec =[]
        for row in self.matrix:
            result=0
            for i in range(0,len(row)):
                result = result + (row[i] * vec[i])
            result_vec.append(result)

        return result_vec

def main():
    v = [1.] * 8  # vector

    m = SparseMatrix2D(rows=10, cols=8)

    m.set(row=0, col=0, value=1.)
    m.set(2, 0, 1.)
    m.set(3, 4, 1.5)
    m.set(3, 3, 1.)
    m.set(7, 6, 1.)
    m.set(5, 2, 5.)
    m.set(0, 0, 2.)

    o = m.solution1(v)
    print(o)
    print(sum(o))

    o=m.solution2(v)
    print(o)
    print(sum(o))

if __name__=='__main__':
    main()