def solution(n):
    answer = 0
    for i in range(n):
        temp = i ** 2
        if temp == n:
            return 1
        elif temp > n:
            return 2
    return answer


print(solution(144))
print(solution(976))

# https://school.programmers.co.kr/learn/courses/30/lessons/120909