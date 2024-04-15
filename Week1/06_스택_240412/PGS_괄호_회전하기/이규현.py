# 아이디어
## 체크하는 배열로 괄호짝이 맞는지 확인

# 예상 시간복잡도
## O(N^2)

# 풀이시간 
## 20분

# 실행시간 
## 0.01ms~ 401.20ms

from collections import deque
def solution(s):

    s = deque(s)
    ans = 0

    for _ in range(len(s)):
        val = s.popleft()
        s.append(val)
        check = []
        
        for i in range(len(s)):

            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                check.append(s[i])
            else:
                if check:
                    if s[i] == '}' and check[-1] == '{':
                        check.pop()
                    elif s[i] == ']' and check[-1] == '[':
                        check.pop()
                    elif s[i] == ')' and check[-1] == '(':
                        check.pop()
                else:
                    check.append(s[i])

        if not check:
            ans += 1

    return ans
