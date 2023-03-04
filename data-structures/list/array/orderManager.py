'''
주문 관리 시스템 (배열)
이번 실습 문제에서는 주문 관리 시스템을 구현합니다. 이 주문 관리 시스템은 총 3가지 기능을 지원해야 합니다. 이는 주문생성, 주문취소, 주문조회입니다. 각각의 자세한 설명은 다음과 같습니다.

주문생성: 고객이 쇼핑몰에서 주문을 하게 되면 이 주문은 고유의 주문번호를 갖게 되고,
이 주문번호가 주문 관리 시스템에 등록됩니다. 물론 고객은 여러 명이기 때문에 주문관리시스템
내에 등록된 주문 번호가 여러 개 있을 수 있으며, 먼저 주문을 한 주문번호가 먼저 처리되는
구조입니다.
주문취소: 고객의 요청에 따라 주문은 취소가 될 수도 있습니다. 주문이 취소될 경우에는 그 주문은 주문 관리 시스템으로부터 삭제됩니다.
주문조회: 주문이 몇 번째로 처리가 될지를 알려줍니다.
이번 실습문제에서는 orderManager class내의 함수 addOrder, removerOrder, getOrder를 통해 위 기능을 구현합니다.

addOrder(x) : 주문번호 x를 주문 관리 시스템에 추가합니다. return 값은 없습니다.
removeOrder(x) : 주문번호 x를 주문 관리 시스템에서 제거합니다. 입력되는 x 값은 항상 주문 관리 시스템에 존재함이 보장됩니다. return 값은 없습니다.
getOrder(x) : 입력한 주문번호 x가 주문 관리 시스템에서 몇 번째로 처리되는지를 return 합니다. 만약 입력한 주문번호 x가 주문 관리 시스템 내에 존재하지 않는 경우 -1을 return 합니다.
예를 들어, addOrder(1), addOrder(2), addOrder(4)를 차례로 실행하면 주문 관리 시스템에 1 - 2 - 4로 입력된 순서대로 저장됩니다. 이 상태에서 removeOrder(2)를 실행하면 주문 관리 시스템에서 주문번호 2를 찾아낸 다음 제거하여 1 - 4 로 주문 관리 시스템이 업데이트됩니다.

이 상황에서 getOrder(1)를 실행한 결과는 주문번호 1이 처리될 순서인 1이 반환되며, getOrder(4)를 실행한 결과는 주문번호 4가 처리될 순서인 2가 반환될 것입니다.

입력 예시
10
1 1
1 2
1 4
2 2
3 1
3 4
1 2
2 1
1 1
3 2

출력 예시
1
2
2

입력 예시2
10
1 4
1 8
3 8
1 2
1 1
2 4
3 8
1 59
1 5959
3 59

출력 예시2
2
1
4
'''

class orderManager :
    def __init__(self) :
        self.data = []

    def addOrder(self, orderId) :
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        for i in range(len(self.data)):
            if self.data[i] == orderId:
                return (i + 1)

        return -1
