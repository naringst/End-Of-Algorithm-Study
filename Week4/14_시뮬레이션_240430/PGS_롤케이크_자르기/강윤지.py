# 아이디어
## 처음 방식은 시간 초과가 발생하여 누적합과 같은 방식으로 풀었다. 주석 참고

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 25분

# 실행시간 
## 8.88ms~ 648.61ms

# 시간초과 O(N^2)
# def solution(topping):
#     answer = 0
#     # 앞에서부터 보면서 가지수 찾기
#     # 일단 총 종류 몇개인지 확인
#     total = len(set(topping))
#     # 이거 절반부터 시작
#     idx = total//2
#     for i in range(idx, len(topping)-idx):
#         first = len(set(topping[:i+1]))
#         second = len(set(topping[i+1:]))
#         if first == second:
#             answer+= 1
#     return answer

def solution(topping):
    answer = 0
    # 누적합!
    # 왼쪽, 오른쪽 나머지 것들 보다가 없는거 있으면 뺸다
    # 왼쪽은 set, 오른쪽은 dict
    forward = set()
    backward = {}
    
    for i in topping:
        if i in backward:
            backward[i] += 1
        else:
            backward[i] = 1
    
    for i in topping:
        # 이젠 앞에서부터 보면서 backward를 하나씩 뺀다
        backward[i] -= 1
        forward.add(i)
        if backward[i] == 0:
            del backward[i]
        if len(forward) == len(backward.keys()):
            answer+=1
    return answer
