def solution(progresses, speeds):
    answer = []
    pointer = 0
    for i in range(100):
        for j in range(len(progresses)):
            progresses[j] = progresses[j] + speeds[j]
            if(progresses[j]>100):
                progresses[j] = 100
    
    
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

pointer = 1
for pointer in range(2):
    print("hello")
print(solution(progresses, speeds))