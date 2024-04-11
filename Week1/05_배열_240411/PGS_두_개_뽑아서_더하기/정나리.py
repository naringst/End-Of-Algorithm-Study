# 아이디어 
## 정렬한 뒤, 두 숫자를 선택해 더한다. 중복되지 않는 수를 반환해야 하니 set으로 answer를 둔다. 
## 이후 오름차순 정렬을 위해 배열로 변환하여 정렬한다. 

# 예상 시간복잡도
## 정렬 NlogN
## for문 N^2, 단 numbers의 길이가 100 이므로 10000번의 계산은 ok

# 풀이시간 
## 20분

# 실행시간 
## 0.01~0.55ms


def solution(numbers):
    answer = set([])

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)) :
            answer.add(numbers[i] + numbers[j])

    result = list(answer)
    result.sort()
    
    return result