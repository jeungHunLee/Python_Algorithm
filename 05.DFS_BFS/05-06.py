# 05-06 (괄호 변환)
def solution(p):
    if not p:  # 빈 문자열이 전달될 경우, 빈 문자열 반환
        return ''

    u = ''
    v = ''
    for i in range(len(p)):
        u += p[i]
        if u.count('(') == u.count(')'):
            v += p[i + 1:]
            break

    if u[0] == '(' and u[len(u) - 1] == ')':  # u가 올바른 문자열이라면
        return u + solution(v)

    else:  # u가 올바른 문자열이 아니라면
        result1 = '(' + solution(v) + ')'

        u = u[1:]  # 첫번째 문자 제거
        u = u[:len(u) - 1]  # 마지막 문자 제거

        result2 = ''
        for i in range(len(u)):
            if u[i] == '(':
                result2 += ')'
            else:
                result2 += '('

        return result1 + result2
