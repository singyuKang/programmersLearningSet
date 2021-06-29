def solution(phone_book):
    answer = true
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = false
            break
    return answer

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))