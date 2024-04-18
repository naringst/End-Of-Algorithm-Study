# 아이디어
## 딕셔너리가 서로 일치하면 카운트하면 된다고 생각

# 예상 시간복잡도
## O(N)보다 클 것 같습니다

# 풀이시간 
## 25분

# 실행시간 
## 0.03ms~ 170.31ms

from collections import Counter
def solution(want, number, discount):
    ans = 0
    item = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        
        if item == c:
            ans += 1
            
    return ans
