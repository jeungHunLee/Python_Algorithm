# 04-10 (기둥과 보 설치)
def solution(n, build_frame):
    answer = []
    for target in build_frame:

        if target[3] == 1:  # 설치
            if target[2] == 0:  # 기둥을 설치하는 경우
                if target[0] < 0 or target[0] > n or target[1] < 0 or target[1] > n - 1:  # 범위의 벗어나는 경우 무시
                    continue
                elif target[1] == 0:  # 바닥인 경우
                    answer.append(target[0:3])
                elif [target[0] - 1, target[1], 1] in answer:  # 보의 오른쪽에 기둥을 설치하는 경우
                    answer.append(target[0:3])
                elif [target[0], target[1], 1] in answer:  # 보의 왼쪽에 기둥을 설치하는 경우
                    answer.append(target[0:3])
                elif [target[0], target[1] - 1, 0] in answer:  # 기둥 위에 기둥을 설치한는 경우
                    answer.append(target[0:3])
                else:
                    continue

            else:  # 보를 설치하는 경우
                if target[0] < 0 or target[0] > n - 1 or target[1] < 0 or target[1] > n:  # 범위를 벗어나는 경우 무시
                    continue
                elif target[1] == 0:  # 보를 바닥에 설치하는 경우 무시
                    continue
                elif [target[0], target[1] - 1, 0] in answer or [target[0] + 1, target[1] - 1,
                                                                 0] in answer:  # 보의 한쪽 끝에 기둥이 있는 경우
                    answer.append(target[0:3])
                elif [target[0] - 1, target[1], 1] in answer and [target[0] + 1, target[1],
                                                                  1] in answer:  # 양 끝에 보가 있는경우
                    answer.append(target[0:3])
                else:
                    continue

        else:  # 삭제
            if target[2] == 0:  # 기둥을 삭제하는 경우
                if [target[0], target[1] + 1, 0] in answer:  # 기둥 위에 기둥이 있을 경우 무시
                    continue
                elif ([target[0], target[1] + 1, 1] in answer and (
                        [target[0] - 1, target[1] + 1, 1] not in answer or [target[0] + 1, target[1] + 1,
                                                                            1] not in answer)):  # 기둥 위에 보가 있고 양 옆으로 보가 연결되지 않은 경우 무시
                    continue
                else:
                    answer.remove(target[0:3])

            else:  # 보를 삭제하는 경우
                if [target[0] + 1, target[1], 0] in answer and [target[0] + 1, target[1] - 1, 0] not in answer:
                    continue  # 보의 오르쪽에 기둥이 있고 기둥 밑에 기둥이 없는 경우 무시
                elif [target[0] - 1, target[1] - 1, 0] not in answer or [target[0] + 1, target[1] - 1, 0] not in answer:
                    continue
                else:
                    answer.remove(target[0:3])

    answer.sort()
    return answer

print(solution(100, [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]))