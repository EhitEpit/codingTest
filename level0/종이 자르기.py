def solution(m, n):
    if m == n == 1:
        answer = 0
    else:
        answer = m * n-1

    return answer


print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))

# https://school.programmers.co.kr/learn/courses/30/lessons/120922
