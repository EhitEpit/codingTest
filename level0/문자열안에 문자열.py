def solution(str1, str2):
    answer = 0
    if str1.count(str2) > 0:
        answer = 1
    else:
        answer = 2
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))

# https://school.programmers.co.kr/learn/courses/30/lessons/120908