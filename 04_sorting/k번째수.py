def solution(array, commands):
    answer = []
    for i in commands:
        newarray = []
        start = i[0]-1
        end = i[1]-1
        select = i[2]
        for a in range(start,end+1):
            newarray.append(array[a])
        newarray.sort()
        answer.append(newarray[select-1])
        
        
        
    
    
    return answer