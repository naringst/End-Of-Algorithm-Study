# 아이디어
## n/2보다 종류가 적다면 답은 종류일 수 밖에 없음, 아니라면 답은 n/2

# 시간복잡도
## O(n)

# 실행시간
## 0.00ms-1.77ms

from collections import defaultdict
def solution(nums):
    
    d = defaultdict(int)
    for val in nums:
        d[val] += 1
    
    if len(d) < len(nums) // 2:
        return len(d)
    else:
        return len(nums) // 2
