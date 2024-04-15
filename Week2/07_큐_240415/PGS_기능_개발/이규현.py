# 아이디어
## 시간을 기준으로 증가하며 카운트하기
## 덱 자료구조 사용

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 20분

# 실행시간 
## 0.01ms~ 0.04ms


from collections import deque
def solution(progresses, speeds):
    dq_p = deque(progresses)
    dq_s = deque(speeds)

    ans = []
    cnt = 0
    day = 0
    while dq_p:
        if (dq_p[0] + day * dq_s[0]) >= 100:
            pg = dq_p.popleft()
            sp = dq_s.popleft()
            cnt += 1            

        else:
            if cnt > 0:
                ans.append(cnt)
                cnt = 0
            else:
                day += 1
    ans.append(cnt)
        
    return ans
