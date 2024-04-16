# 아이디어
## 문자열을 순회하며 하나씩 스택에 넣고, 짝이 맞으면 하나씩 뺸다.

# 예상 시간복잡도
## s의 문자열 길이만큼 for 문 순회 -> 1,000,000 백만번 
## 1초 안에 풀이 가능

# 풀이시간 
## 10 분

# 실행시간 
## 0.0ms~ 18.99ms

def solution(s):
    answer = 0
    stack =[]
    
    for i in range(len(s)) :
        if stack and s[i] == stack[-1] :
            stack.pop()
            continue
        else :
            stack.append(s[i])
    
    if not stack :
        answer = 1

    return answer