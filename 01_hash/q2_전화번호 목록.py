# 20210518
def solution(phone_book):
    d = dict()
    for n in phone_book:
        d[n] = 0
    for n in phone_book:
        t = ""
        for c in n[:-1]:
            t += c
            if (t not in d):
                return False
    return True