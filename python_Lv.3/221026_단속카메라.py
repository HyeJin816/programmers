def solution(routes):
    routes = sorted(routes)
    answer = 1
    
    ### 카메라 구간
    cam_s = routes[0][0]
    cam_e = routes[0][1]
    
    for car in routes:
        if car[0] > cam_e:
            answer += 1
            cam_s = car[0]
            cam_e = car[1]
        else:
            cam_s = max(cam_s, car[0])
            cam_e = min(cam_e, car[1])
    
    return answer
