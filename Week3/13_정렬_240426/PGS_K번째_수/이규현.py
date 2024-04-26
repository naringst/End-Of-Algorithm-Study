# 아이디어
## 자르고 정렬

# 예상 시간복잡도
## O(coomands 수)

# 풀이시간 
## 5분

# 실행시간 
## 0.00ms~ 0.01ms

def solution(array, commands):
    answer = []
    
    for command in commands:
        s, e, idx = command
        new_array = array[s-1:e]
        new_array.sort()
        answer.append(new_array[idx-1])
    return answer
