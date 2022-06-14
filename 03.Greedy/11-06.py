# 무지의 먹방 라이브
# 예시 풀이
import heapq

def solution(food_times, k):
    # 전체 시간이 k시간 보다 같거나 적다면 -1 반환
    if sum(food_times) <= k:
        return -1

    q = []  # 우선순위 큐를 저장할 새로운 배열
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0   # 현재 먹기 위해 사용한 시간
    previous = 0    # 직전 번호에 다 먹은 시간
    length = len(food_times)    # 남은 음식의 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1     # 다 먹은 음식은 개수에서 제외
        previous = now  # 이전 음식을 현재 음식으로 변경

    result = sorted(q, key = lambda x: x[1])    # 튜플의 두번째 값을 key로 설정하여 정렬
    return result[(k - sum_value) % length][1]