# 15 -29 (공유기 설치)
import sys
n, c = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        gap = (start + end) // 2
        count = 1
        router = array[0]    # 현재 설치된 공유기 위치
        for i in range(1, n):
            if array[i] - router >= gap:
                count += 1
                router = array[i]
        if count >= target:
            result = gap
            start = gap + 1
        else:
            end = gap - 1
    return result


start = 1
end = array[-1] - array[0]
print(binary_search(array, c, start, end))