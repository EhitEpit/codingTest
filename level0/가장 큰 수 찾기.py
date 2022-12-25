def solution(array):
    answer = []
    num = max(array)
    answer.append(num)
    answer.append(array.index(num))
    return answer


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

# https://school.programmers.co.kr/learn/courses/30/lessons/120899
