# 04-07(문자열 압축)
# 나의 풀이
def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        compress, tmp, count = "", "", 1
        for j in range(0, len(s), i):
            if s[j:j + i] == tmp:
                count += 1
            else:
                compress += str(count) + tmp if count > 1 else tmp
                tmp = s[j:j + i]
                count = 1
        compress += str(count) + tmp if count > 1 else tmp
        answer = min(answer, len(compress))
    return answer

# 예시 풀이
def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):  # 1개부터 len(s) // 2까지 개수로 압축하는 모든 경우의 수
        compressed = ""  # 압축된 문자열을 저장할 빈 문자열
        count = 1  # 반복되는 문자열의 수
        prev = s[0:i]  # i개 만큼 압축하는 첫번째 문자열 추출
        for j in range(i, len(s), i):   # i부터 len(s)-1까지 i만큼 증가
            if s[j: j + i] == prev:  # 문자열을 추출하여 첫번째 문자열과 일치 여부 확인
                count += 1
                continue
            else:
                compressed += chr(count) + prev if count >= 2 else prev  # count = 1일때 1은 생략
                prev = s[j: j + i]  # 초기화
                count = 1  # 초기화
        # 나머지 문자열에 대하여 처리
        compressed += chr(count) + prev if count >= 2 else prev  # count = 1일때 1은 생략
        answer = min(answer, len(compressed))
    return answer