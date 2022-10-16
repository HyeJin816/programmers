def solution(genres, plays):
    ### 데이터 정리
    total = []
    for z in zip(genres, enumerate(plays)):
        total.append(z)

    ### 장르 횟수 정렬
    gen = {}
    for g in total:
        if g[0] not in gen:
            gen[g[0]] = int(g[1][1])
        else:
            gen[g[0]] += int(g[1][1])
    gen = sorted(gen, key=lambda x: gen[x], reverse=True)

    answer = []
    for g in gen:
        check = [x for x in total if x[0]==g]
        check = sorted(check, key = lambda x : x[1][1], reverse=True)
        answer.append(check[0][1][0])
        if len(check) >= 2:
            answer.append(check[1][1][0])

    return answer
