# 아이디어
## 결국 나보다 우선순위가 높은 애들은 나보다 '먼저' 나간다.
## => 따라서 나보다 우선순위가 높은 애들의 개수를 세서 count에 더한다.
## 나머지 중 나와 우선순위가 같은 애들만 고려하면 된다. 우선순위가 낮은 애들은 나보다 늦게 나가기 때문이다.
## => 따라서 나보다 우선순위 높은 애들을 처리할 때, 누가 마지막으로 처리되는지 그 인덱스를 저장한다. 
## 이때, 마지막으로 처리되는 애의 인덱스는 나보다 큰 값중 가장 작은 값이 된다. 그 마지막 처리된 애를 기준으로 나와 같은 값들끼리 순서를 정해준다.

## => 하지만 이풀이는 틀림

# 다시 푼 아이디어
## priorities를 deque로 만들고,
## priorities의 원소를 꺼내면서 location을 하나 앞으로 당겨준다.
## 이렇게 해야 하는 이유는 원소를 꺼내면 내가 목표로 하는 location의 인덱스가 바뀌기 때문이다.
## 그리고 all 문법을 사용해 현재 priorities의 있는 모든 원소보다 top이 이상일 때, 그니까 최댓값일때 지금 꺼낸 값이 내가 꺼내려던 값(loaction == -1)이라면 answer+1를 출력한다. 
## 몇 번째로 출력되는지를 구해야 하기 때문에 앞선 pop된 개수+1을 해준다.
## 내가 원하는 타겟 값은 아니지만 배열 중 최댓값이면 꺼낸 것의 개수만 세준다. (answer+=1)
## 그리고 최댓값이 아니라면 다시 뒤로 append해주는데, 이때 내가 꺼낸 값이 location이었다면 인덱스를 바꿔줘야 하므로 location을 다시 맨 뒷 인덱스로 지정해준다.

# 예상 시간복잡도
## O(priorities배열 수 * priorities 배열 수) == O(100*100)

# 풀이시간 
## 50분 + 알파

# 실행시간 
## 0.01ms~ 0.55ms

from collections import deque

def solution(priorities, location):
    curr_idx = 0
    answer = 0 
    priorities = deque(priorities)
    
    while priorities :
        top = priorities.popleft()
        location -= 1

        if all(top>= num for num in priorities) :
            if location == -1 :
                return answer + 1
            else :
                answer +=1
        else :
            priorities.append(top)
            if location == -1 :
                location = len(priorities) - 1
    
    return answer


    