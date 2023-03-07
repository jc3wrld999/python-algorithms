import math

def mergeSort(data) :
    '''
    합병정렬이란 리스트를 2부분으로 나누어 각각을 정렬하고 비교하여 합치는 정렬로 O(nlogn)의 시간복잡도를 가진다.
    '''
    
    if len(data) == 1:
        return data
        
    result = []

    mid = len(data)//2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    lPtr = 0
    rPtr = 0

    while lPtr < len(left) or rPtr < len(right):
        lValue = left[lPtr] if lPtr < len(left) else math.inf
        rValue = right[rPtr] if rPtr < len(right) else math.inf

        if lValue < rValue:
            result.append(lValue)
            lPtr += 1
        else:
            result.append(rValue)
            rPtr += 1
    return result

def main():
    # test case
    data = [1, 5, 6, 2, 3, 8, 4, 9, 7, 10]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()
