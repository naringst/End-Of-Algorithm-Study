# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

def solution(n, k, cmd):
    deleted = []
    
    for command in cmd:
        line = command.split()
        
        if line[0] == "D":
            k += int(line[1])
            # 행 벗어나는지 판단
            if k > n - len(deleted):
                k = n - len(deleted)
        if line[0] == 'U':
            k -= int(line[1])
            # 행 벗어나는지 판단
            if k < 0:
                k = 0
        if line[0] == 'C':
            deleted.append(k)
            # 만약, 제일 마지막거 지운다면, k는 -1
            if k == n - len(deleted):
                k -= 1
        if line[0] == 'Z':
            item = deleted.pop()
            # 만약 이게 현재 k 보다 작다면, k 는 추가
            if item < k:
                k += 1
    
    answer = ['O' for _ in range(n)]
    for item in deleted:
        answer[item] = 'X'
        
    return "".join(answer)