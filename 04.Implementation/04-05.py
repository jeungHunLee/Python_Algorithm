# 04-05 (럭키 스트레이트)
# 나의 풀이
score = input()
head = score[:len(score) // 2]
tail = score[len(score) // 2:]

head = list(map(int, head))
tail = list(map(int, tail))

if sum(head) == sum(tail):
    print("LUCKY")
else:
    print("READY")

# 예시 풀이
n = input()
left = 0
right = 0

for i in range(len(n) // 2):
    left += int(n[i])

for i in range(len(n) // 2, len(n)):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")