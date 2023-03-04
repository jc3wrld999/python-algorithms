def findKth(myInput, k) :
    '''
    k번째 수 찾기
    n개의 숫자가 차례대로 주어질 때, 매 순간마다 “지금까지 입력된 숫자들 중에서 k번째로 작은 수”를 반환하는 프로그램을 작성하세요.
    '''
    result = []
    myList = []
    for i in myInput:
        myList.append(i)
        myList.sort()
        result.append(myList[k-1] if len(myList) >= k else -1)
    return result

def main():
    firstLine = [10, 3]
    myInput = [1, 9, 8, 5, 2, 3, 5, 6, 2, 10]

    print('정렬 결과: ', *findKth(myInput, firstLine[1]))
if __name__ == "__main__":
    main()
