def solution(my_string, num1, num2):
    my_string = list(my_string)
    temp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = temp
    return ''.join(my_string)


print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))


# https://school.programmers.co.kr/learn/courses/30/lessons/120895
