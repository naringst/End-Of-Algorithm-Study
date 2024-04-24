# 아이디어
## 주석 참고
## 질문하기 및 교재 참고하여 문제 해결

# 예상 시간복잡도
## O(N^2)

# 풀이시간 
## _ 분

# 실행시간 
## 0.01ms~ 329.93ms

# from sys import setrecursionlimit
# setrecursionlimit(10000)

# def solution(nodeinfo): ### ↓ n:노드번호 추가하여 (x,y,n) 형태로 x좌표 기준 정렬
#     result = [[],[]]
#     nodeinfo = sorted([(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)], key=lambda x:x[0])

#     # 재귀 함수 선언
#     def REC(nodeinfo):
#         if not nodeinfo:
#             return
#         # 계속 반복해서 도는겨
#         highest = (0, -1, 0) # idx, y, n
#         # 계속 돌면서 제일 상위 노드 찾기 = y가 제일 높은거 찾기
#         for idx, (x, y, n) in enumerate(nodeinfo):
#             if y > highest[1]:
#                 highest = (idx, y, n)
#         # 다 돌았으면 = 루트 노드 찾았으면 이제 전위순회!
#         result[0].append(highest[-1])
#         left, right = nodeinfo[:highest[0]], nodeinfo[highest[0]+1:]
#         REC(left), REC(right)
#         result[1].append(highest[-1])
        
#     REC(nodeinfo)
    
#     return result


from collections import deque

class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info # 좌표
        self.left = left # 왼쪽 자식 노드
        self.right = right # 오른쪽 자식 노드
        self.num = num # 번호
        
    # 왼쪽 자식 노드가 있는지 확인
    def has_left(self):
        return self.left is not None
    
    # 오른쪽 자식 노드가 있는지 확인
    def has_right(self):
        return self.right is not None
    
# 이진 트리 생성 함수
def make_BT(nodeinfo):
    # 노드의 번호 리스트 생성
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    # [7, 4, 2, 6, 1, 3, 9, 8, 5]
    
    # 정렬
    nodes.sort(key=lambda x: (nodeinfo[x-1][1], -nodeinfo[x-1][0]), reverse=True)
    root = None
    
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodeinfo[nodes[0] -1], nodes[0]) # 좌표, 번호
        else:
            parent = root
            node = Node(nodeinfo[nodes[i] - 1], nodes[i]) # 좌표, 번호
            
            while True:
                # 부모 노드의 x 좌표가 더 크면 자식 노드는 왼쪽으로
                if node.info[0] < parent.info[0]:
                    # 만약 부모 노드의 왼쪽 노드가 있다면
                    if parent.has_left():
                        # 그 노드의 자식노드로 들어간다
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                # 부모 노드의 x 좌표가 더 작으면 자식 노드는 오른쪽으로
                else:
                    # 만약 부모 노드의 오른쪽 노드가 있다면
                    if parent.has_right():
                        # 그 오른쪽 자식의 자식으로 들어간다
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    return root
                    
            

# 전위 순회
def pre_order(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)

# 후위 순회
def post_order(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

def solution(nodeinfo): ### ↓ n:노드번호 추가하여 (x,y,n) 형태로 x좌표 기준 정렬
    # 결과를 저장할 리스트
    answer = [[], []]
    
    # 이진 트리 생성
    root = make_BT(nodeinfo)
    
    # print(root)
    # 전위 순회
    pre_order(root, answer)
    
    # 후위 순회
    post_order(root, answer)
    
    return answer