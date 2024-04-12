arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]

length = len(arr1[0])

for i in range(0, len(arr1)):
    for j in range(0, len(arr2[0])):
        for k in range(length):
            answer[i][j] += arr1[i][k] * arr2[k][j]

print(answer)

# 2 3 2   5 4 3
# 4 2 4   2 4 1
# 3 1 4   3 1 1

# 1*1 = 1,1
# 1*2 = 1,2

# 1 2   2
#       1