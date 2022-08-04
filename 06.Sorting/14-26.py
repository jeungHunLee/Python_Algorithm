# 14-26 카드 정렬하기
import heapq
n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    heapq.heappush(numbers, number)

numbers.sort()
result = 0

while len(numbers) != 1:
    num1, num2 = heapq.heappop(numbers), heapq.heappop(numbers)
    result += (num1 + num2)
    heapq.heappush(numbers, num1 + num2)

print(result)
