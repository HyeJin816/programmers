def solution(skill, skill_trees):
    answer = 0
    skill = list(map(str,str(skill)))
    for i in range(len(skill_trees)):
        # trees에서 skill 원소만 추출
        skill_trees[i] = [x for x in skill_trees[i] if x in skill]
    # skill과 trees 비교
    for i in skill_trees: 
        count = 0
        for j in i:
            if i.index(j) == skill.index(j):
                count += 1
        if count == len(i):
            answer += 1
    return answer
