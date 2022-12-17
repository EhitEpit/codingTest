def solution(num, total):
    answer = []
    middle_num = total / num
    max_count = int(num / 2)
    if total % num == 0:
        answer.append(int(middle_num))
    else:
        answer.append(int(middle_num))
        answer.append(int(middle_num)+1)
        max_count -= 1

    for i in range(1, max_count + 1):
        answer.insert(0, answer[0] - 1)
        answer.append(answer[len(answer) - 1] + 1)
    return answer


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))

# https://school.programmers.co.kr/learn/courses/30/lessons/120923
