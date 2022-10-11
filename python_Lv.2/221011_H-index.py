def solution(citations):
    answer = 0
    citations = sorted(citations)
    for i in range(len(citations)//2, max(citations)):
        check = [x for x in citations if x>=i]
        if len(check) >= i:
            answer = i
    return answer
