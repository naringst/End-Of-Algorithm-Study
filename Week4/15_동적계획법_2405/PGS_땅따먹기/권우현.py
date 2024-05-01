land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    answer = 0
    land = [[0]+i+[0] for i in land]
    for i in range(1, len(land)):
        for j in range(1, 5):
            land[i][j] += max(max(land[i-1][:j]), max(land[i-1][j+1:]))

    return max(land[-1])

print(solution(land))
