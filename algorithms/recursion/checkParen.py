def checkParen(data):
    if len(data) == 0:
        return True
    elif len(data) == 1:
        return False
    if data[0] != "(":
        return False
    for idx, a in enumerate(data):
        if a == ")":
            data2 = data[:idx-1] + data[idx+1:]
            return checkParen(data2)
    return False

x = "(((())())(()())((())()))"
print(checkParen(x))
    
