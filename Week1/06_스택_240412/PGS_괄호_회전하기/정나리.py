# 아이디어
## 닫히는 괄호는 여는 괄호 바로 다음에 오기 떄문에, 스택에 담으면서 열린 괄호 뒤 닫힌 괄호가 오는지 확인한다.

# 예상 시간복잡도
## O(s) == O(1000)

# 풀이시간 
## 15분

# 실행시간 
## 0.00ms~ 125.89ms


# 괄호가 열리고 그 다음에 바로 닫히면 제거
def isRightString(s) :
        answer = False
        stack = []
    
        for i in range(len(s)) :
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                stack.append(s[i])
            else :
                if s[i] == ')':
                    if stack and stack[-1] == '(' :
                        stack.pop()
                    else :
                        return answer
                elif s[i] == ']' :
                    if stack and stack[-1] == '[' :
                        stack.pop()
                    else :
                        return answer
                elif s[i] == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else :
                        return answer 
        if not stack :
            answer = True
        
        return answer


def solution(s):
    answer = 0
    for i in range(len(s)) :
        new_s = s[i:] + s[:i] 
        if isRightString(new_s) :
            answer +=1 

    
    return answer