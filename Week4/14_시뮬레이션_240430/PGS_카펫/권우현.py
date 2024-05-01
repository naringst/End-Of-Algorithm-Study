import math

brown, yellow = 24,24

def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0 and (i+2)*((yellow//i)+2) == brown+yellow:
            Max = max(i, yellow//i)
            Min = min(i, yellow//i)
            return [Max+2, Min+2]


def solution2(brown, yellow):
    k = (brown - 4)//2
    answer1 = int((+k-math.sqrt(k*k-4*yellow))/2)
    answer2 = int((+k+math.sqrt(k*k-4*yellow))/2)
    return [answer2+2, answer1+2]


print(solution(brown, yellow))
print(solution2(brown, yellow))