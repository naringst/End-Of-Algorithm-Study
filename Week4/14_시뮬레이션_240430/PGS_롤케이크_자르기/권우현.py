import collections

topping = [1, 2, 1, 3, 1, 4, 1, 2]

left = set()
right = set()
left_sum = []
right_sum = []
answer = 0
for i in range(len(topping)):
    left.add(topping[i])
    right.add(topping[len(topping) - i - 1])
    left_sum.append(len(left))
    right_sum.append(len(right))
print(left_sum)
right_sum = (right_sum[::-1])
print(right_sum)

for i in range(1, len(right_sum)):
    if right_sum[i] == left_sum[i - 1]:
        answer += 1

print(answer)