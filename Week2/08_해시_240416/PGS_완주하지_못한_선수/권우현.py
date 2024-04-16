# 아이디어
## 정렬해서 다르면 return

# 예상 시간복잡도
## nlogn

# 풀이시간
## 10분

# 실행시간
## 0.00ms~ 75.07msms

completion = ["stanko", "ana", "mislav"]
participant = ["mislav", "stanko", "mislav", "ana"]
answer = ''

completion.sort()
participant.sort()

for i in range(len(completion)):
    if completion[i] != participant[i]:
        print(participant[i])

print(participant[len(participant)-1])