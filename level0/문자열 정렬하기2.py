def solution(my_string):
    answer = ''.join(sorted(my_string.lower()))
    return answer


print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))


# https://school.programmers.co.kr/learn/courses/30/lessons/120911