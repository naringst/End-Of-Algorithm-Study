# 경로를 어떻게 저장해야하는지 고민
# () -> 튜플은 수정할 수 없기에 먼저 sorted 후 tuple로 다시 저장
# 저장된 경로 길이 반환

def solution(dirs):    
    # U, D, L, R
    directions = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    
    # 현재 위치, 다음 위치
    cur_x, cur_y = 0, 0
    next_x, next_y = 0, 0
    
    # 방문 표시
    visited = set([])
    
    for i in dirs:
        dx, dy = directions[i]
        
        # 명령어대로 다음 경로 설정
        next_x = cur_x + dx
        next_y = cur_y + dy

        # 만약, 경로 벗어나는 명령어라면 무시
        if (-5 > next_x or next_x > 5 or -5 > next_y or next_y > 5):
            continue
        
        # 지금 방문한 곳 set에 넣기
        # 정렬 필요 - 순서가 중요한게 아니라 경로가 중요하다.
        visited.add(tuple(sorted(((next_x, next_y), (cur_x, cur_y)))))
        
        cur_x = next_x
        cur_y = next_y        
    
    return len(visited)