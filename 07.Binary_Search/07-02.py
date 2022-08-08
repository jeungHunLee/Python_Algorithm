# 07-02 (떡볶이 떡 만들기)
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

def binary_search(numbers, target, start, end):
    answer = []
    while start <= end:
        result = 0
        mid = (start + end) // 2
        for i in range(n):
            if numbers[i] > mid:
                result += numbers[i]-mid
            else:
                continue

        if result >= target:
            answer.append(mid)
            start = mid + 1
        else:
            end = mid - 1

    return max(answer)

print(binary_search(numbers, m, 0, max(numbers)))