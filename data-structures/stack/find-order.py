'''
계산 순서 정하기
괄호 p가 주어질 때, 각 괄호가 몇 번째로 계산되어야 하는 괄호인지를 list로 반환합니다.

예를 들어, p='(()())' 일 경우, [3, 1, 1, 2, 2, 3] 을 반환합니다.

예시
(()()) >> 3 1 1 2 2 3
(())() >> 2 1 1 2 3 3
((())(())()) >> 6 2 1 1 2 4 3 3 4 5 5 6
((((())((())()))())()) >> 11 9 7 2 1 1 2 6 4 3 3 4 5 5 6 7 8 8 9 10 10 11

'''
import stack as stack

def find_order(p) :

    s = stack.Stack()
    cnt = 0 # 괄호 개수 세기
    result = [0] * len(p)

    for i in range(len(p)):
        if p[i] == '(':
            s.push(i)
        else:
            top = s.top() # 최근 여는 괄호
            
            cnt += 1
            result[top] = cnt # (
            result[i] = cnt # )

            s.pop()

    return result