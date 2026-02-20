def solution(name:list, yearning:list, photo):
    answer = []
    len_photo = len(photo)

    for i in range(len_photo):
        len_p = len(photo[i])
        mem = 0
        for j in range(len_p):
            n = photo[i][j]
            
            if n in name:
                k = name.index(n)
                mem += yearning[k]

        answer.append(mem)
        
    return answer