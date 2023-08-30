if __name__ == '__main__':
    arr = []
    scr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        scr.append(score)
    temp = min(scr)
    while temp in scr:
        scr.remove(temp)
    name = []
    for i in arr:
        if i[1] == min(scr):
            name.append(i[0])
    name = sorted(name)
    for i in name:
        print(i)
        
