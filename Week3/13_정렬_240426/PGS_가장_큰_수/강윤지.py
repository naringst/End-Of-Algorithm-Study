# 아이디어
## 문자열로 변환하여 바로 옆 값과 문자열을 더해 차이를 비교한다.
## [6, 10, 2] 인 경우, 610과 106 중 어느것이 더 큰지를 비교하여 구하였다.

# 예상 시간복잡도
##

# 풀이시간 
## 45분

# 실행시간 
## 0.03ms~ 2120.93ms

import functools

def solution(numbers):    
    # 일단 문자열로 변환
    str_list = list(map(str, numbers))

    def compare(a, b):
        return (int(a+b)-int(b+a))

    sorted_num = sorted(str_list, key = functools.cmp_to_key(lambda a, b : compare(a, b)), reverse=True)

    return str(int("".join(sorted_num)))

# 다른 풀이
## numbers의 원소는 1000 이하이기에, 각 원소를 문자열로 치환한 뒤, 3을 곱해주어 비교해주었다
## 예를 들어 [3, 30, 34, 5, 9]의 경우 [3333, 30303030, 34343434,5555, 9999]로 바뀐 뒤,
## 이를 내림차순 정렬하여 구하였다. 숫자로 크기 비교하는게 아닌, 문자열 비교인 것에 주의한다
def solution(numbers):    

    str_list = list(map(str, numbers))
    sorted_num = sorted(str_list, key=lambda x: x*3, reverse=True)

    return str(int("".join(sorted_num)))