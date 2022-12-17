def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer


print(solution(2, 10))
print(solution(7, 15))

# 이런;; >> 비트연산자 잊고 있었네

# https://school.programmers.co.kr/learn/courses/30/lessons/120910