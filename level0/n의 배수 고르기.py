def solution(n, numlist):
    return list(filter(lambda x: x % n == 0, numlist))


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5, [1, 9, 3, 10, 13, 5]))
print(solution(12, [2, 100, 120, 600, 12, 12]))

# https://school.programmers.co.kr/learn/courses/30/lessons/120905
