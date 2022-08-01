# 06-02 (성적이 낮은 순서로 학생 출력하기)
n = int(input())
student = []

for _ in range(n):
    student.append(list(input().split()))

result = sorted(student, key=lambda x: x[1])

for i in range(n):
    print(result[i][0], end=" ")