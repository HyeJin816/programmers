def solution(s):
  
    answer = 1
    l = len(s)
    
    for start in range(l):
        for back in range(start+1,l+1):
            check = s[start:back]
            if len(check) < answer:
                continue
            elif check == check[::-1]:
                answer = max(answer, back-start)

    return answer
