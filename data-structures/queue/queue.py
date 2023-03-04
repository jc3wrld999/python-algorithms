'''
입구와 출구가 각각 한쪽 끝에 존재하는 자료구조

구성
- head
- rear

기능
- push: rear위치에 자료를 추가하고 rear를 1 증가시킴
- pop: head위치에 자료를 제거하고 head를 1 증가시킴
- front
- back
- empty
'''
class Queue:

    def __init__(self) :
        self.myQueue = []

    def push(self, n) :
        self.myQueue.append(n)

    def pop(self) :
        if(self.empty()==0):
            del self.myQueue[0]

    def size(self) :
        return len(self.myQueue)

    def empty(self) :
        return 1 if self.size() == 0 else 0

    def front(self) :
        return -1 if self.empty() else self.myQueue[0]

    def back(self) :
        return -1 if self.empty() else self.myQueue[-1]
        
        

