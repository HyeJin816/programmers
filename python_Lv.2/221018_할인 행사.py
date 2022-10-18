def solution(want, number, discount):
    answer = 0
    want_dict = {want[i] : number[i] for i in range(len(want))}

    for i in range(len(discount)-sum(number)+1):
        temp_dict = dict()
        for j in range(i,i+sum(number)):
            if discount[j] in temp_dict.keys():
                temp_dict[discount[j]] += 1
            else:
                temp_dict[discount[j]] = 1

        if temp_dict == want_dict:
            answer += 1

    return answer 
