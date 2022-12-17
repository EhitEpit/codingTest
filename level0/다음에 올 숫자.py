def solution(common):
    answer = 0

    num1 = common[1] - common[0]
    num2 = common[2] - common[1]
    if num1 == num2:
        answer = common.pop() + num1
    else:
        num1 = int(common[1] / common[0])
        num2 = int(common[2] / common[1])
        if num1 == num2:
            answer = common.pop() * num1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))


# https://school.programmers.co.kr/learn/courses/30/lessons/120924