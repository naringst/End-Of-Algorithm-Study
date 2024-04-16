# 아이디어
## goal에 popleft로 빼고 card1, card2에 잇나 확인.


# 예상 시간복잡도
##

# 풀이시간
## 10분

# 실행시간
## 0.01ms~ 0.05ms

from collections import deque

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

goal = deque(goal)
flag = True

while len(goal) > 0:
    target = goal.popleft()
    if cards1 and target == cards1[0]:
        cards1.remove(target)
    elif cards2 and target == cards2[0]:
        cards2.remove(target)
    else :
        flag = False
        break

answer = ""
if flag == True:
    answer = "Yes"
else : answer = "No"

print(answer)