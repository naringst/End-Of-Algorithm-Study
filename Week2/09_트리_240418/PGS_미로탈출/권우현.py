# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
minTimeLever = 10000
minTimeExit = 10000
def solution(maps):
    global minTimeLever
    global minTimeExit
    location = [0, 0]
    locationLever = [0, 0]
    for i in range(len(maps)):
        flag = False
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                location[0] = i
                location[1] = j
                flag = True
                break
        if flag:
            break
    for i in range(len(maps)):
        flag = False
        for j in range(len(maps[0])):
            if maps[i][j] == "L":
                locationLever[0] = i
                locationLever[1] = j
                flag = True
                break
        if flag:
            break
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[location[0]][location[1]] = True

    moveToLever(0, location[0], location[1], False, visited, maps)

    visited[location[0]][location[1]] = False
    visited[locationLever[0]][locationLever[1]] = True
    moveToExit(0, location[0], location[1], False, visited, maps)
    if(minTime == 10000):
        return -1
    else:
        return (minTimeLever+minTimeExit)

def moveToLever(time, now_x, now_y, lever, visited, maps):
    global minTimeLever
    print("time ", time)
    print("now_x ", now_x)
    print("now_y ", now_y)
    print()
    if maps[now_x][now_y] == "L":
        minTimeLever = min(minTimeLever, time)
        return
    if maps[now_x][now_y] == "L":
        lever = True
    #왼쪽, 오른쪽 , 위 , 아래
    if now_x - 1 >= 0 and maps[now_x][now_y] in {'O', 'L'} and not visited[now_x - 1][now_y]:
        visited[now_x - 1][now_y] = True
        moveToLever(time + 1, now_x - 1, now_y, lever, visited, maps)
    if now_x + 1 < len(maps) and maps[now_x][now_y] in {'O', 'L'} and not visited[now_x + 1][now_y]:
        visited[now_x + 1][now_y] = True
        moveToLever(time + 1, now_x + 1, now_y, lever, visited, maps)
    if now_y - 1 >= 0 and maps[now_x][now_y] in {'O', 'L'} and not visited[now_x][now_y - 1]:
        visited[now_x][now_y-1] = True
        moveToLever(time + 1, now_x, now_y - 1, lever, visited, maps)
    if now_y + 1 < len(maps[0]) and maps[now_x][now_y] in {'O', 'L'} and not visited[now_x][now_y + 1]:
        visited[now_x][now_y + 1] = True
        moveToLever(time + 1, now_x, now_y + 1, lever, visited, maps)

def moveToExit(time, now_x, now_y, lever, visited, maps):
    global minTimeExit
    print("time ", time)
    print("now_x ", now_x)
    print("now_y ", now_y)
    print()
    if maps[now_x][now_y] == "L":
        minTimeExit = min(minTimeExit, time)
        return
    if maps[now_x][now_y] == "L":
        lever = True
    #왼쪽, 오른쪽 , 위 , 아래
    if now_x - 1 >= 0 and maps[now_x][now_y] in {'O', 'E'} and not visited[now_x - 1][now_y]:
        visited[now_x - 1][now_y] = True
        moveToLever(time + 1, now_x - 1, now_y, lever, visited, maps)
    if now_x + 1 < len(maps) and maps[now_x][now_y] in {'O', 'E'} and not visited[now_x + 1][now_y]:
        visited[now_x + 1][now_y] = True
        moveToLever(time + 1, now_x + 1, now_y, lever, visited, maps)
    if now_y - 1 >= 0 and maps[now_x][now_y] in {'O', 'E'} and not visited[now_x][now_y - 1]:
        visited[now_x][now_y-1] = True
        moveToLever(time + 1, now_x, now_y - 1, lever, visited, maps)
    if now_y + 1 < len(maps[0]) and maps[now_x][now_y] in {'O', 'E'} and not visited[now_x][now_y + 1]:
        visited[now_x][now_y + 1] = True
        moveToLever(time + 1, now_x, now_y + 1, lever, visited, maps)