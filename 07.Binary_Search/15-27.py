# 15-27 (정렬된 배열에서 특정 수의 개수 구하기)
from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
numbers = list(map(int, input().split()))

left = bisect_left(numbers, x)
right = bisect_right(numbers, x)

if left == right:
    print(-1)
else:
    print(right - left)

# 이진 탐색
# 처음 위치를 찾는 이진 탐색 함수
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:    # 해당 원소 중 가장 왼쪽에 위치한 인덱스 반환
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 함수
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:    # 해당 원소 중 가장 오른쪽에 위치한 인덱스 반환
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

# x의 개수를 찾는 함수
def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n - 1)

    if a == None:
        return 0
    b = last(array, x, 0, n - 1)
    return b - a + 1

n, x = map(int, input().split())
numbers = list(map(int, input().split()))

count = count_by_value(numbers, x)

if count == 0:
    print(-1)
else:
    print(count)