def solution(s1, s2):
    answer = 0
    for item in s1:
        if item in s2:
            answer += 1

    return answer


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))

# https://school.programmers.co.kr/learn/courses/30/lessons/120903
