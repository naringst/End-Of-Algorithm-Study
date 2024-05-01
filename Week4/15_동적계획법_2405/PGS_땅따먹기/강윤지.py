# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 9분

# 실행시간 
## 2.13ms~ 209.26ms

def solution(land):
    for i in range(1, len(land)):
        # 직전 행 중 같은 열 제외한 것들 중 최댓값 찾기
        for j in range(4):
            temp = land[i-1][:j] + land[i-1][j+1:]
            max_value = max(temp)
            # 해당 칸 업데이트
            land[i][j] += max_value

    return max(land[-1])
