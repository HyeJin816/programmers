def solution(s):
    s = s[2:-2].split('},{')

    ### 튜플 리스트 분리
    change = []
    for letters in s:
        nums = letters.split(",")
        nums = list(map(int, nums))
        change.append(nums)

    ### 길이순정렬 
    change = sorted(change, key = lambda x: len(x))

    ### 결과 출력
    answer = []
    for nums in range(len(change)):
        for n in change[nums]:
            if n not in answer:
                answer.append(n)

    return answer
