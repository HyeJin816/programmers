import itertools

def solution(elements):
    answer = []
    
    ### 길이 for문
    for i in range(1,len(elements)+1):
        ### 시작 for문
        elm = elements+elements
        for e in range(len(elm)):
            arr = sum(elm[e:e+i])
            answer.append(arr)

    answer = set(answer)
    return len(answer)
