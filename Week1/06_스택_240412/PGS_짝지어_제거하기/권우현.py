# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

s = 'baabaa'
s = list(s)
for i in range(len(s)-1):
    print(i)
    if s[i] == s[i+1]:
        s.pop(i+1)
        s.pop(i)
        i-=1
print(s)