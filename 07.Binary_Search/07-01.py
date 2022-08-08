# 07-01 (부품 찾기)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None;

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
request = list(map(int, input().split()))

for target in request:
    result = binary_search(array, target, 0, n - 1)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')