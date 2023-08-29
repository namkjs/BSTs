if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0, N):
        s = input()
        temp = s.split()
        if 'insert' in s:
            arr.insert(int(temp[1]), int(temp[2]))
        elif 'print' in s:
            print(arr)
        elif 'remove' in s:
            arr.remove(int(temp[1]))
        elif 'append' in s:
            arr.append(int(temp[1]))
        elif 'sort' in s:
            arr.sort()
        elif 'pop' in s:
            arr.pop()
        elif 'reverse' in s:
            arr.reverse()