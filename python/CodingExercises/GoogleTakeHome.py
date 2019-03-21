'''
A sample state of ‘a’:
[[2, NULL, 2, NULL],
[2, NULL, 2, NULL],
[NULL, NULL, NULL, NULL],
[NULL, NULL, NULL, NULL]]
FUNCTION foo()
    FOR y = 0 to 3
        FOR x = 0 to 3
	    IF a[x+1][y] != NULL
	        IF a[x+1][y] = a[x][y]:
	            a[x][y] := a[x][y]*2
	            a[x+1][y] := NULL
                 END IF
	         IF a[x][y] = NULL
                     a[x][y] := a[x+1][y]
	             a[x+1][y] := NULL
                 END IF
              END IF
          END FOR
    END FOR
END FUNCTION
'''
def GoogleTakeHome(ary):

    for i in range(0,len(ary)):
        for j in range(0,len(ary[i])):
            if ary[j][i]!=None:
                if ary[j][i]==ary[j][i]:
                    ary[j][i]=ary[j][i]*2
                    ary[j][i]=None
                if ary[j][i]==None:
                    ary[j][i]=ary[j][i]
                    ary[j][i]=None
    print(ary)

def main():

    ary=[[2, None, 2, None],
         [2, None, 2, None],
         [None, None, None, None],
         [None, None, None, None]]
    print(GoogleTakeHome(ary))

if __name__=='__main__':
    main()