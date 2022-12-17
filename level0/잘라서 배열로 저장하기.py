def solution(my_str, n):
    answer = []

    while my_str != "":
        answer.append(my_str[:n])
        my_str = my_str[n:]

    return answer


print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))

# https://school.programmers.co.kr/learn/courses/30/lessons/120913