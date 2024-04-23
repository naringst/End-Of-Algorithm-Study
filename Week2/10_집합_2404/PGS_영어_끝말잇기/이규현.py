# 아이디어
## 단어 하나씩 집합에 집어넣어 길이 비교 + 끝글자 첫글자 비교

# 예상 시간복잡도
## O(words의 길이)

# 풀이시간 
## 20분

# 실행시간 
## 0.01ms~ 0.03ms

def solution(n, words):
    answer = [0,0]
    s = set()
    last_char = words[0][0]
    for idx, word in enumerate(words):

        s.add(word)        
        if len(s) != (idx+1) or last_char != word[0]:
            answer[0] = (idx % n) + 1
            answer[1] = (idx // n) + 1
            break
        last_char = word[-1]     
        
    return answer
