'''
올바른 괄호인지 판단하기
예를 들어, ‘(())’ 은 올바른 괄호이지만, ‘(()))’, 혹은 ‘(()()(‘ 는 올바른 괄호가 아닙니다.

예시
(())() >> YES
(((())())(()())((())())) >> YES
(())())() >> NO
)( >> NO
'''
import stack as stack


def check_paren(p) :
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''
    s = stack.Stack()
    for c in p:
        if c == '(':
            s.push(c)
        else:
            if s.empty():
                return "NO"
            s.pop()
    if s.empty():
        return "YES"
    else:
        return "NO"