# 아이디어
## sort를 해서 앞뒤에 앞쪽 문자열이 같은 순서대로 나열.
## 그리고 뒤 문자열의 길이가 길 때 두 문자열을 비교.

# 예상 시간복잡도
## n = len(phone_book) => nlogn

# 풀이시간 
## ??분

# 실행시간 
## 0.00ms~ 98.22ms

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for p in range(len(phone_book)-1) :
        if len(phone_book[p]) < len(phone_book[p+1]) :
            if phone_book[p+1][:len(phone_book[p])] == phone_book[p] :
                return False
    return answer

## 다른 사람의 풀이 중 해시를 활용한 풀이

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number

            if temp in hash_map and temp != phone_number:
                answer = False
    return answer