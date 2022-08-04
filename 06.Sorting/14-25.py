# 14-25 (실패율)
def solution(N, stages):
    answer = []
    for stage in range(1, N + 1):
        challenger = len([i for i in stages if i >= stage])
        fail = stages.count(stage)
        if challenger == 0:  # 스테이지에 도달한 유저가 없다면 실패율은 0
            failure_rate = 0
        else:
            failure_rate = fail / challenger
        answer.append((stage, failure_rate))  # (스테이지 번호, 실패율)

    answer.sort(key=lambda x: -x[1])  # 내림차순 정렬

    answer = [i[0] for i in answer]

    return answer


# 예시 답안
def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

        answer = sorted(answer, key=lambda x: x[1], reverse=True)

        answer  = [i[0] for i in answer]
        return answer
