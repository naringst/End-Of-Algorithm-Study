# 아이디어
## 슬라이딩 윈도우로 하루 지날때마다 빼고 더해줘서 맞는지 체크

# 예상 시간복잡도
## 10만번 연산

# 풀이시간 
## 25분

# 실행시간 
## 0.01ms~ 57.12ms

want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

n = len(discount)
wanted = dict(zip(want, number))
market = {i:0 for i in want}

s = 0
e = 9
for i in range(0, e+1):
    if discount[i] in market:
        market[discount[i]] += 1
answer = 0
while True:

    if wanted == market:
        answer += 1

    if discount[s] in market:
        market[discount[s]] -= 1
    s += 1
    e += 1
    if e==n:
        break

    if discount[e] in market:
        market[discount[e]] += 1

print(answer)