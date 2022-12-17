def solution(A, B):
    answer = -1
    length = len(A)
    count = 0
    if A == B:
        return 0

    for i in range(length):
        A = A[length-1] + A
        A = A[:length]
        count += 1
        if A == B:
            answer = count
            break

    return answer


print(solution("hello", "hello"))
print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("abcdefg", "bcdefga"))

# https://school.programmers.co.kr/learn/courses/30/lessons/120921