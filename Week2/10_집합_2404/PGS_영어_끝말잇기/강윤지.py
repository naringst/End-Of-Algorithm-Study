# 아이디어
## 주석 참고

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 15분

# 실행시간 
## 0.01ms~ 0.14ms

def solution(n, words):    
    # 제일 먼저 탈락하는 사람의 번호 및 몇번째 차례에 탈락하는지 반환
    user_list = [0] * n
    cur_words = []
    last = words[0][0]

    for i in range(len(words)):
        # 사람 수 만큼 나눈 것의 나머지가 해당 사람의 차례
        # 이전에 했던거인지 어떻게 확인?
        # set으로 만들어서 길이 차이가 나냐 안나냐로 확인
        
        # 해당 사람 횟수 증가
        user_list[i % n] += 1
        cur_words.append(words[i])
        
        # 만약 끝말잇기 실패한다면
        # 같은 단어 반복하는지 검사
        if len(cur_words) != len(set(cur_words)):
            # 만약 반복된다면 끝.
            return [i%n+1, user_list[i%n]]
        # 이전 단어와 이어지지 못할 때
        if not words[i].startswith(last):
            return [i%n+1, user_list[i%n]]
        last = words[i][-1]

    return [0, 0]