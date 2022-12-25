def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except:
        return -1


print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))

# https://school.programmers.co.kr/learn/courses/30/lessons/120904
