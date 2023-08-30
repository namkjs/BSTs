if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    temp = []
    for i in arr:
        temp.append(i)
    a = max(temp)
    while a in temp:    
        temp.remove(a)
    print(max(temp))
