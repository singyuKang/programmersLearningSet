# 20210518
def solution(clothes):
    answer = 1
    d = {}
    for l in clothes:
        if (l[1] in d):
            d[l[1]] += 1
        else:
            d[l[1]] = 2
    for k in d:
        answer *= d[k]
    return answer-1