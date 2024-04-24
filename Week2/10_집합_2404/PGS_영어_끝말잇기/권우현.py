# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms
n = 2
words =	["tank", "kick", "kick", "know"]



used = []
prev = ""
answer = [0, 0]
def chkCorrect(word, prev):
    if not word.startswith(prev):
        return True

    if not len(word) > 1:
        return True

    if word in used:
        return True

    return False

def solution(n, words):
    global prev
    for i in range(len(words)):
        if prev == "":
            used.append(words[i])
            prev = words[i][-1]
            continue

        flag = chkCorrect(words[i], prev)

        if flag:
            if (i+1)%n==0:
                answer[0] = n
                answer[1] = int((i+1)/n)
            else :
                answer[0] = (i+1) % n
                answer[1] = int((i+1)/n)+1
            return answer

        prev = words[i][-1]
        used.append(words[i])

    return answer