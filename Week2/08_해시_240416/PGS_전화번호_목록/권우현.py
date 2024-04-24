# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


phone_book = ["119", "97674223", "1195524421"]

answer = False

phone_book = sorted(phone_book)
for i in range(len(phone_book)-1):
    if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
        print(phone_book[i], phone_book[i+1])

print(answer)