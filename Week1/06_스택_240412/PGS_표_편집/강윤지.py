# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

def solution(n, k, cmd):
    answer = ''
    
    # 삭제한 인덱스 저장
    deleted = []
    
    # up, down
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    
    # 현재 위치
    k += 1
    
    # 명령어 처리
    for line in cmd:
        # 삭제
        if line.startswith('C'):
            # 삭제한 배열에 저장
            deleted.append(k)
            # k 아래, 위 이어주기
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            # 다음 인덱스 처리
                # 만약 마지막 행이라면, 바로 위. 아니라면 아래 행.
            if n < down[k]:
                k = up[k]
            else:
                k = down[k]
        # 복원
        elif line.startswith('Z'):
            # 일단 꺼낸다
            restore = deleted.pop()
            # 자기 위치는 그대로, 자기 아래와 위는 변경
            down[up[restore]] = restore
            up[down[restore]] = restore
        elif line.startswith('U'):
            # k만 변경
            direction, X = line.split()
            # X 만큼 바로 올리는게 아니라, X 만큼 이동한다!
            for _ in range(int(X)):
                k = up[k]
        elif line.startswith('D'):
            direction, X = line.split()
            for _ in range(int(X)):
                k = down[k]
    
    # X 표시
    answer = ["O"] * n
    for i in deleted:
        answer[i-1] = 'X'
    return "".join(answer)