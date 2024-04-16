# 아이디어
## 

# 예상 시간복잡도
## O(n)

# 풀이시간 
## 48분

# 실행시간 
## 0.00ms~ 0.68ms

def solution(priorities, location):
    count = 0
    while priorities:
        if priorities[0] != max(priorities):
            # 우선순위가 가장 큰게 앞으로 올 때 까지 돌린다
            priorities.append(priorities.pop(0))
            location = len(priorities) - 1 if location == 0 else location - 1
        elif location == 0:
            # 맨 앞이 location이라면 끝
            return count + location + 1
        else:
            # 우선순위가 가장 큰걸 큐에서 빼면서, count를 증가시킴
            # 이후 count는 location이 빠진 순서에 이용
            priorities.pop(0)
            count += 1
            location -= 1