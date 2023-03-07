LIMIT_NUMBER = 1000000007

def fillBox(n):
    '''
    2 x n 의 상자를 2 x 1 의 블럭으로 채우는 경우의 수를 구하는 프로그램을 작성하세요. 단, 그 경우의 수가 매우 커질 수 있기 때문에, 경우의 수를 1,000,000,007으로 나눈 나머지를 출력합니다.
    '''
    T = [1, 1]

    for i in range(2, n+1):
        t = T[i-1] + T[i-2]
        T.append(t)
        
    return T[-1] % LIMIT_NUMBER