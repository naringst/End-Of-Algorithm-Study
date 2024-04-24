# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


s = "[)(]"
s = list(s)

stack = []
answer = 0

for i in range(len(s)):  #이동
    flag = True
    for j in range(len(s)):
        n = i + j
        if n >= len(s): n %= len(s)

        if s[n] == "[" or s[n] == "(" or s[n] == "{":
            stack.append(s[n])
        elif s[n] == "]":
            if len(stack) == 0:
                flag = False
                break
            elif stack[-1] != "[":
                flag = False
                break
            else:
                stack.pop()
        elif s[n] == "}":
            if len(stack) == 0:
                flag = False
                break
            elif stack[-1] != "{":
                flag = False
                break
            else:
                stack.pop()
        elif s[n] == ")":
            if len(stack) == 0:
                flag = False
                break
            elif stack[-1] != "(":
                flag = False
                break
            else:
                stack.pop()
    if flag and len(stack) == 0: answer += 1
    stack.clear()
print(answer)
