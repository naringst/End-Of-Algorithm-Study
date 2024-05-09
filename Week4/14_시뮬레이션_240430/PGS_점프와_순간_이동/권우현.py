N = 1

answer = 0
while True:
    print(N)
    if N == 0:
        break
    if N == 1:
        answer += 1
        break
    if N % 2 == 1:
        answer += 1
        N = int(N/2)
    else:
        N = int(N/2)

print("answer = ", answer)