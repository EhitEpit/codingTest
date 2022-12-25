def solution(n):
    answer = 0
    num = str(n)
    for item in num:
        answer += int(item)
    return answer


print(solution(1234))
print(solution(930211))

# https://school.programmers.co.kr/learn/courses/30/lessons/120906
