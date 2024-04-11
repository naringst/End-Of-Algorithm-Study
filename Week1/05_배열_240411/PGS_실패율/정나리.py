# 아이디어 
# 구현. 배열을 순회하며 특정 단계까지 간 사용자 수, 특정 단계에서 멈춰있는 사용자 수를 구하고 이를 나눈다.
# 그리고 실패율을 기준으로 sort 하여 값을 구한다.

# 예상 시간복잡도
# stages 길이 * (1 부터 end까지(N)) => 200,000 * 500 = 100,000,000 => 1억번 연산 => 약 2초

# 풀이시간 35분
# 실행시간 0.02~7594.75ms

def solution(N, stages):
    answer = []
    tried = [0] * (N+1)
    fail = [0] * (N+1)
    
    for i in range(len(stages)) :
        stage = stages[i]
        end = stages[i] + 1
        if stage == N+1 :
            end -= 1
        for j in range(1,end) :
            tried[j] += 1

        if stage < (N +1) :
            fail[stage] += 1
    
    # 여기 시간복잡도 n
    for k in range(1, len(tried)):
        if tried[k] == 0 :
            answer.append([0,k])
        else :
            answer.append([fail[k]/tried[k],k])
    
    answer.sort(key=lambda x:x[0],reverse=True)

    result = []
    for a in range(len(answer)) :
        result.append(answer[a][1])
    
    return result