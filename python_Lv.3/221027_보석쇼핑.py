import collections

def solution(gems):
    answer = []

    count = collections.Counter()
    
    total = len(set(gems))  ### 전체 보석 종류
    left = 0                ### 시작지점
    right = 0               ### 종료지점

    for num in range(len(gems)):
        right += 1
        count[gems[num]] += 1
        while len(count) == total:
            count[gems[left]] -= 1
            if count[gems[left]] == 0:
                del count[gems[left]]
            left += 1
            answer.append([left,right])

    ans = [(ans[1]-ans[0], ans) for ans in answer]
    ans = sorted(ans)

    return ans[0][1]
