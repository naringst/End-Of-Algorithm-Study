# 아이디어
## 앞에 숫자랑 비교해서 다르면 추가


# 예상 시간복잡도
##

# 풀이시간
## 5분

# 실행시간
## 0.01ms~ 0.05ms



arr = [4,4,4,3,3]

answer = []
prev = 11
for i in arr:
    if i == prev:
        pass
    else:
        answer.append(i)
        prev = i

print(answer)