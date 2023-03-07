LIMIT_NUMBER = 1000000007

def getPower(m, n):
    '''
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    만약 getPower 함수의 반환 값이 1,000,000,000,007 보다 클 경우, 반환 값을 1,000,000,000,007로 나눈 나머지 값을 반환하세요.

    입력
    3 4
    출력
    81
    '''
    if n == 0:
        return 1

    if n % 2 == 0:
        return getPower(m, n/2)**2 % LIMIT_NUMBER
    else:
        return getPower(m, (n-1)/2)**2 * m % LIMIT_NUMBER

def main():

    myList = [int(v) for v in input().split()]

    print(getPower(myList[0], myList[1]))

if __name__ == "__main__":
    main()
