# 문자열 재정렬
# 나의 풀이
s = input()
numbers = []        # 문자열에서 숫자를 저장할 배열
alphabet = []         # 문자열에서 알파벳을 저장할 배열
new_string = ""

for i in range(len(s)):         # 문자열을 하나씩 순회하며 숫자와 알파벳을 구분
    if 65 <= ord(s[i]) <= 90:
        alphabet.append(s[i])
    else:
        numbers.append(int(s[i]))

alphabet.sort()     # 알파벳 오름차순 정렬

for i in range(len(alphabet)):      # 알파벳을 하나씩 새로운 문자열에 연결
    new_string += alphabet[i]

if sum(numbers) != 0:       # numbers의 값이 존재한다면 새로운 문자열 뒤에 연결
    new_string += str(sum(numbers))

print(new_string)

# 예시 풀이
data = input()
result = []
value = 0

for i in range(data):   # 문자열을 하나씩 확인
    if i.isalpha():     # 알파벳이면 result 리스트에 추가
        result.append(i)
    else:
        value += i      # 숫자이면 value에 더하기

result.sort()   # 알파벳 오름차순 정렬

if value != 0:      # 숫자가 존재한다면 result 가장 뒤에 추가
    result.append(str(value))

print(''.join(result))  # resut 리스트의 요소를 연결



