def solution(s):
    answer = ''
    for item in s:
        if s.count(item) == 1:
            answer += item
    return ''.join(sorted(answer))


print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))

# https://school.programmers.co.kr/learn/courses/30/lessons/120896
