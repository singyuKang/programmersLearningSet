import heapq

def solution2(scoville, K):
    answer = 0
    heap = []
    
    for number in scoville:
        heapq.heappush(heap, number)
        
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) *2))
        except IndexError:
            return -1
        answer +=1
    return answer


def solution1(scoville, K):
    answer = 0
    
    while(min(scoville) < K ):
        scoville.sort()
        first_scoville = scoville[0]
        second_scoville = scoville[1]
        count_scoville = first_scoville + second_scoville*2
        del scoville[0]
        del scoville[0]
        scoville.insert(0, count_scoville)
        # print(scoville)
        answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution1(scoville, K))