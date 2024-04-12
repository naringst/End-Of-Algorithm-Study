real = input()
real = list(map(int, real.split()))

answer1 = [1, 2, 3, 4, 5] * 2000
answer2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

correct = [0, 0, 0]

for i in range(0, len(real)):
    if real[i] == answer1[i]:
        correct[0] += 1
    if real[i] == answer2[i]:
        correct[1] += 1
    if real[i] == answer3[i]:
        correct[2] += 1

first = max(correct)
answer = []
for i in range(len(correct)):
    if correct[i]==first: answer.append(i+1)

print(real)
print(correct)
print(answer)