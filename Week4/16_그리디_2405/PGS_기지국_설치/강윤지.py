# 아이디어
## list에 직접 기록하는 풀이를 시도해봤는데, 시간 초과 발생. 
## station들 사이에 몇 개의 기지국을 설치해야 하는지 푸는 방식으로 해결

# 예상 시간복잡도
##

# 풀이시간 
## 73분

# 실행시간 
## 0.00ms~ 2.96ms

def solution(n, stations, w):
    answer = 0
    end = 0
    
    for station in stations:
        left = station - w - 1
        right = station + w
        distance = left - end # 기존 end 로부터 새로운 기지국의 왼쪽 끝까지의 거리 계산
        
        # 새로운 기지국이 필요한 경우
        if distance > 0:
            answer += distance // (2*w+1)
            if distance % (2*w+1):
                answer += 1   
                
        end = right # end를 새로운 기지국의 오른쪽 끝으로 업데이트
        
    # 마지막 기지국 이후 남은 공간 처리
    if end < n:
        distance = n - end
        answer += distance // (2*w+1)
        if distance % (2*w+1):
            answer += 1

    return answer
