# numbers = [2,1,3,4,1]
numbers = [5,0,2,7]

answer = set()
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        answer.add(numbers[i]+numbers[j])

print(answer)