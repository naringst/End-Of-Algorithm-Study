# 아이디어
## 정렬 후 한개씩 비교

# 예상 시간복잡도
## O(n)

# 풀이시간 
## 35분

# 실행시간 
## 0.01ms~ 2.05ms

from collections import defaultdict
def solution(phone_book):

    h = defaultdict(int)
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        h[phone_book[i]] += 1
        l = len(phone_book[i])
        if phone_book[i+1][:l] in h:
            return False
    return True
