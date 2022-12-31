## Stack

- 어떤 작업이 다른 작업보다 먼저 이뤄져야 하는 경우
- 스택 활용 예시
    - 콜 스택(Call Stack): 컴퓨터 프로그램에서 현재 실행 중인 함수(서브루틴)을 저장하는 역할
    - 스택은 의존관계가 있는 상태를 저장함
    - factorial(재귀)
        ```python
        def factorial(n):

            if(n==0):
                return 1
            return n * factorial(n-1)
        ```
    - 
