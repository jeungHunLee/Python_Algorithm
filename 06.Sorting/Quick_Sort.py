# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # left부터 array[pivot]보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right부터 array[pivot]보다 작은 데이터를 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:    # 엇갈리면 right와 pivot 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 정렬 후 왼쪽 부분과 오른쪽 부분에 대하여 다시 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)