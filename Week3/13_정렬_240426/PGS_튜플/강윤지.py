# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 60분

# 실행시간 
## 0.03ms~ 257.27ms

def solution(s):
    answer = []
    
    # 맨 앞, 뒤 짜르기
    s = s[2:-2]
    
    # },{ 로 자르기
    s = s.split('},{')
    
    # 각 요소들 ,로 자르기
    s = [i.split(',') for i in s]

    # zip으로 하나의 리스트로 만들기
    s = sum(s, [])
    
    temp = [0]*len(s)
    num_dict = dict(zip(s, temp))
    
    # 리스트 돌면서 빈도 파악
    for i in range(len(s)):
        # 딕셔너리에 추가
        num_dict[s[i]]+=1

    # 값의 내림차순으로 정렬
    temp2 = dict(sorted(num_dict.items(), key=lambda x: x[1], reverse=True))
    
    # 순서대로 키 반환
    answer = list(map(int, temp2.keys()))
    return answer