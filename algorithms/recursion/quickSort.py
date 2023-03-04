def quickSort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]

    left = getSmallNumbers(data[1:], pivot)
    right = getLargeNumbers(data[1:], pivot)

    return quickSort(left) + [pivot] + quickSort(right)

def getSmallNumbers(data, pivot):
    l = []
    for elem in data:
        if elem <= pivot:
            l.append(elem)
    return l

def getLargeNumbers(data, pivot):
    l = []
    for elem in data:
        if elem > pivot:
            l.append(elem)
    return l