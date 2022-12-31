# 한쪽 끝에서만 자료를 넣고 뺄 수 있는 구조(LIFO)

# 주요 기능
# push 
# pop
# top
# empty: 스택이 비어있는지 여부를 확인

class Stack:

    def __init__(self) :
        self.myStack = []

    def push(self, n) :
        self.myStack.append(n)

    def pop(self) :
        if(self.size() ==0):
            return
        else:
            self.myStack.pop()

    def size(self) :
        return len(self.myStack)

    def empty(self) :
        if(self.size() ==0):
            return 1
        else:
            return 0

    def top(self) :
        if(self.empty() == 1):
            return -1
        else:
            return self.myStack[-1]