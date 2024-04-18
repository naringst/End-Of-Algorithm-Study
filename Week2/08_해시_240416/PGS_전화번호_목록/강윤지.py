# 아이디어
## 문자열 리스트인 phone_book을 정렬하여, 앞 숫자가 비슷한 것끼리 붙여둔다.
## 양 옆을 비교하여 return 값을 결정한다

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 11분

# 실행시간 
## 0.00ms~ 104.07ms

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
    