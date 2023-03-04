'''
링크드 큐 구현하기
파이썬 내장 라이브러리에서 제공하는 큐 자료구조는 연결 리스트를 기반으로 구현되어 있습니다.
큐 자료구조를 구현하되, 배열 대신 연결 리스트를 사용하여 구현해보도록 하겠습니다.

지시사항
첫 번째 줄에 큐가 수행할 연산의 개수를 나타내는 정수 n이 입력됩니다. (1≤n≤10000)

두 번째 줄부터 n개의 줄에 걸쳐 큐가 수행할 연산을 입력합니다.

1 x : 큐에 정수 x를 입력
2 : 큐에서 정수를 제거
3 : 큐의 size 출력
4 : 큐가 비어있는지 여부 출력
5 : 큐의 head 값 출력
6 : 큐의 rear 값 출력

입력 예시
7
1 1
1 2
1 3
3
4
5
6

출력 예시
3
0
1
3
'''

class LinkedListElement :
    def __init__(self, val, p, n) :
        self.value = val
        self.myPrev = p
        self.myNext = n
        
class Queue:
    def __init__(self) :
        self.start = None
        self.end = None
        self.count = 0

    def push(self, n) :
        '''
        덱에 정수 n을 맨 뒤에 넣습니다.
        '''
        if self.start == None and self.end == None :
            elem = LinkedListElement(n, None, None)
            self.start = elem
            self.end = elem
        else :
            elem = LinkedListElement(n, self.end, None)
            self.end.myNext = elem
            self.end = elem
        
        self.count += 1
        return

    def pop(self) :
        '''
        덱에서 가장 앞에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1 :
            return
        
        if self.count >= 2 :
            nextNode = self.start.myNext
            nextNode.myPrev = None
            self.start = nextNode
        else :
            self.start = None
            self.end = None
        
        self.count -= 1
        return

    def size(self) :
        '''
        덱에 들어 있는 정수의 개수를 return 합니다.
        '''
        return self.count

    def empty(self) :
        if self.size() == 0 :
            return 1
        return 0

    def front(self) :
        if self.empty() == 1 :
            return -1
        return self.start.value

    def back(self) :
        if self.empty() == 1 :
            return -1
        return self.end.value