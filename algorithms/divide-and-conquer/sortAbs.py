def sortAbs(array):
    '''
    절댓값을 기준으로 오름차순 정렬한 결과를 반환하는 함수를 작성하세요.
    '''

    return array 

def main():
    line = [int(x) for x in input().split()]

    print(*sortAbs(line))

if __name__ == "__main__":
    main()
