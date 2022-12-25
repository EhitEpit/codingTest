def solution(my_string):
    answer = 0
    list1 = my_string.split(' ')
    isAdd = True
    for item in list1:
        if item == '-':
            isAdd = False
        elif item == '+':
            isAdd = True
        else:
            if isAdd:
                answer += int(item)
            else:
                answer -= int(item)
    return answer


print(solution("3 + 4"))


# eval 이라는 내장 함수가 있는데 이걸 쓰면 매개변수로 받은 식형태의 문자열을 계산해줌.
# 다만 거의 모든 식을 계산하기 때문에 운영에서는 보안의 위험이 있을 것 같음.
# eval("3 + 4") = 7

# https://school.programmers.co.kr/learn/courses/30/lessons/120902
