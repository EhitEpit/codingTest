def solution(babbling):
    answer = 0
    word_list = ["aya", "ye", "woo", "ma"]
    for item in babbling:
        for word in word_list:
            item = item.replace(word, " ")
        if item.strip() == "":
            answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))

# https://school.programmers.co.kr/learn/courses/30/lessons/120956
