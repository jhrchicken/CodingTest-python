def solution(n):
    answer = []
    while n > 0:
        answer.append(int(n % 10))
        n = int(n / 10)
    return answer