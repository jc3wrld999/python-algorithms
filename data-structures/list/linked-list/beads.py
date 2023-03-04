'''
구슬 넣기 (연결 리스트)

n개의 구슬이 있으며, 각 구슬은 1부터 n까지의 번호를 하나씩 갖고 있습니다. 또한, 양 쪽이 뚫려있고 투명하지 않은 관을 갖고 있습니다.
n개의 구슬을 이 파이프에 무작위로 넣은 후에, 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 암기함으로써 암기력을 높이려고 합니다.
파이프의 왼쪽에, 혹은 오른쪽에 구슬을 넣을 수 있습니다. 예를 들어, 파이프의 왼쪽으로 숫자 1의 구슬을 넣고, 파이프의 오른쪽으로 숫자 3의 구슬을 넣고, 마지막으로 파이프의 왼쪽으로 숫자 2의 구슬을 넣게 되면, 최종적으로 구슬의 배치는 2 1 3 이 됩니다.
n개의 구슬을 파이프에 넣는 행위가 입력으로 주어질 때, 최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력하는 프로그램을 작성하세요.

(단, 파이프의 길이는 n개의 구슬을 모두 담기에 충분히 길다고 가정합니다.)
'''

class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = val
        self.myNext = ptr

class LinkedListPipe:
    def __init__(self) :
        self.start = None
        self.end = None
        pass

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None)
            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, self.start)
            self.start = elem


    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None)
            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, None)
            self.end.myNext = elem
            self.end = elem

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        result = []
        current = self.start

        while current != None:
            result.append(current.value)
            current = current.myNext
        return result

def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = LinkedListPipe()

    for bead, direction in myInput:
        print(bead, direction)
        if direction == 0:
            myPipe.addLeft(bead)
        elif direction == 1:
            myPipe.addRight(bead)
    return myPipe.getBeads()