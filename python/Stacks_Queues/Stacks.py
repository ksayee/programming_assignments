class Stack:

    def __init__(self):
        self.stk=[]

    def push(self,data):
        self.stk.append(data)

    def pop(self):
        return self.stk.pop()

    def printstk(self):
        for data in (self.stk):
            print(data)

    def isEmpty(self):
        return self.stk==[]

def main():

    s=Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.printstk()
    s.pop()
    print(s.isEmpty())
    s.printstk()
    s.pop()
    s.pop()
    print(s.isEmpty())


if __name__=='__main__':
    main()