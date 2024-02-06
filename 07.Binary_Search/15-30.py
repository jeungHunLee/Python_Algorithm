# 15-30 가사 검색
# 나의 풀이
def compare(a, b):
    isMatching = True

    for i in range(len(a)):
        if b[i] != '?' and a[i] != b[i]:
            isMatching = False

    return isMatching

def find_left(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if compare(arr[mid], target):
            if mid == 0 or not compare(arr[mid - 1], target):
                return mid
            else:
                end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

def find_right(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if compare(arr[mid], target):
            if mid == len(arr) - 1 or not compare(arr[mid + 1], target):
                return mid
            else:
                start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i] = sorted(array[i])
        reversed_array[i] = sorted(reversed_array[i])

    for query in queries:
        if query[-1] == '?':
            new_words = array[len(query)]
        else:
            new_words = reversed_array[len(query)]
            query = query[::-1]

        left, right = find_left(new_words, query), find_right(new_words, query)

        if left is None or right is None:
            answer.append(0)
        else:
            answer.append(right - left + 1)

    return answer

# 예시 풀이
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i] = sorted(array[i])
        reversed_array[i] = sorted(reversed_array[i])

    for query in queries:
        if query[-1] == '?':
            new_words = array[len(query)]
        else:
            new_words = reversed_array[len(query)]
            query = query[::-1]

        answer.append(count_by_range(new_words, query.replace('?', 'a'), query.replace('?', 'z')))

    return answer