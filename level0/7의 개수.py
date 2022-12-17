def solution(array):
    answer = 0
    array = list(map(lambda x: str(x), array))
    for item in array:
        answer += item.count('7')
    return answer


print(solution([7, 77, 17]))
print(solution([10, 29]))

# https://school.programmers.co.kr/learn/courses/30/lessons/120912