# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

user = {}
answer = []

for record in records:
    record = record.split()
    if record[0] == "Enter":
        user[record[1]] = record[2]
    elif record[0] == "Change":
        user[record[1]] = record[2]
    else: continue

for record in records:
    record = record.split()
    if record[0] == "Enter":
        answer.append(user[record[1]]+"님이 들어왔습니다.")
    elif record[0] == "Leave":
        answer.append(user[record[1]]+"님이 나갔습니다.")
    else: continue
print(answer)