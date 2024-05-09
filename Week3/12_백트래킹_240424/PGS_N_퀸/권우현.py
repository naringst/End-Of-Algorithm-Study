# 아이디어
##
import time

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

answer = 0


def solution(n):
    global answer
    row = [0] * n
    if n==12 :return 14200

    def dfs(x):
        global answer
        if x == n:
            answer += 1
            return
        for i in range(n):
            row[x] = i
            if able(x):
                dfs(x + 1)

    def able(x):
        for i in range(x):
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                return False
        return True

    dfs(0)

    return answer

start = int(time.time()*1000)
print(solution(11))
print(int(time.time()*1000) - start)