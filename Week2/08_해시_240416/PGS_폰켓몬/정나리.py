# 아이디어
## 전체 포켓몬 중 절반 개수를 골라가기 때문에 종류의 개수를 먼저 체크한다. 
## 이를 위해 nums를 포켓몬 종류에 따라 dict로 만든다.
## 그리고 dict의 길이인 포켓몬 종류 수가 절반보다 작으면 그 수가 답이 된다.
## 절반이 넘는다면 절반의 수가 서로 다른 포켓몬의 수가 된다.

# 예상 시간복잡도
## Counter에 걸리는 시간 복잡도 == O(10,000 == nums 길이)

# 풀이시간 
## 10분

# 실행시간 
## 0.02ms~ 1.36ms

from collections import Counter
def solution(nums):
    answer = 0
    total_num = len(nums)//2
    
    dict = Counter(nums)
    
    if len(dict) <= total_num :
        answer = len(dict)
    else :
        answer = total_num        
    
    return answer