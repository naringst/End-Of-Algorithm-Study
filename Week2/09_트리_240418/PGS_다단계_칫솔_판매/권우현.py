# 아이디어
##

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

import math

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

recommends = dict(zip(enroll, referral))

sell = dict(zip(seller, amount))
money = {i: 0 for i in enroll}
amount = [i * 100 for i in amount]

for i in range(len(seller)):
    name = seller[i]
    now = amount[i]
    recommend = recommends[name]
    money[name] += amount[i] - math.floor(now * 0.1)

    while recommend != "-":
        name = recommend
        recommend = recommends[recommend]
        now = math.floor(now * 0.1)
        if now == 0:
            break
        money[name] += now - math.floor(now * 0.1)

answer = []
for name in enroll:
    answer.append(money[name])

print(answer)
