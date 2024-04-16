# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

def isCorrect(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])

        elif (len(stack) == 0):
            return False
        if s[i] == ')' and stack[-1] == '(':
            stack.pop()

        if s[i] == '}' and stack[-1] == '{':
            stack.pop()
        if s[i] == ']' and stack[-1] == '[':
            stack.pop()
            
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0

    if len(s) % 2 != 0:
        return 0

    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if isCorrect(rotated):
            answer += 1
        
    return answer