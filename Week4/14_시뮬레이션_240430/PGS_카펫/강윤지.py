# 아이디어
## 주석 참고

# 예상 시간복잡도
## O(logN)

# 풀이시간 
## 23분

# 실행시간 
## 0.00ms~ 0.18ms

def solution(brown, yellow):
    # 노란색 크기 먼저 정한 다음, 갈색 맞는지 확인
    
    # 노란색 크기 다 고려해보기
    # 제일 작은 것 부터 고려해보기
    height = 1
    while True:
        # 1부터 yellow 까지 다 돈다
        if yellow % height != 0:
            # 만약 공약수가 아니라면 다음거 돈다
            height += 1
            continue
        # 만약 세로가 더 크다면
        width = yellow // height
        if height > width:
            break
        # 만약 공약수라면        
        # brown 갯수 맞는지 확인
        # brown = 2*width + 2 *(height + 2)
        if brown == 2 * width + 2 * (height + 2):
            return [width+2, height+2]
        height += 1
        