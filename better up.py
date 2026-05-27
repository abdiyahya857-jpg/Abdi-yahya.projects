n = int(input())
elements = input().split()

numbers = []
for item in elements:
    numbers.append(int(item))

while -1 in numbers:
    numbers.remove(-1)

answer = sum(numbers) / len(numbers)
print(answer)
