def solution(record):

    talk = {}
    for r in record:
        r = r.split(' ')
        if r[0] == 'Leave':
            continue
        if r[0] == 'Change':
            del talk[r[1]]
        talk[r[1]] = r[2]
        
    answer = []
    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            line = talk[r[1]]+'님이 들어왔습니다.'
            answer.append(line)
        elif r[0] == 'Leave':
            line = talk[r[1]]+'님이 나갔습니다.'
            answer.append(line)
        
    return answer
