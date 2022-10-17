def solution(n):
    world = [4,1,2]
    answer = ''

    while n:
        answer = str(world[n%3]) + answer
        if n%3 ==0:
            n = n//3 -1
        else:
            n = n//3

    return answer
