def solution(quiz):
    answer = []
    for str1 in quiz:
        temp = str1.split(" = ")
        if " - " in temp[0]:
            if int(temp[0].split(" - ")[0]) - int(temp[0].split(" - ")[1]) == int(temp[1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(temp[0].split(" + ")[0]) + int(temp[0].split(" + ")[1]) == int(temp[1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))

# https://school.programmers.co.kr/learn/courses/30/lessons/120907