def binarySearch(data, m) :
    '''
    이진 탐색
    n개의 숫자 중에서 m이 존재하면 "Yes", 존재하지 않으면 "No"를 반환하는 함수를 작성하세요.
    '''
    if len(data) == 0:
        return "No"
    elif len(data) == 1:
        return "Yes" if data[0] == m else "No"

    mid = len(data)//2
    if data[mid] == m:
        return "Yes"
    elif data[mid] > m:
        return binarySearch(data[:mid], m)
    else:
        return binarySearch(data[mid:], m)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [1, 4, 6, 7, 10, 14, 16]
    m = int(input())

    print(binarySearch(data, m))

if __name__ == "__main__":
    main()
