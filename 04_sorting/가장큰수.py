from itertools import permutations

def solution(numbers):
    arrayLength = len(numbers)
    stringArray = []

    for i in range(arrayLength):
        stringArray.append(str(numbers[i]))
    b=[]
    for i in list(permutations(stringArray)):
        b.append(i)
    c=[]
    for i in range(len(b)):
        putArray = ''.join(b[i])
        c.append(putArray)
    numberArray = []

    for i in range(len(c)):
        numberArray.append(int(c[i]))
    numberArray.sort()
    maxNumber = numberArray[len(numberArray)-1]
    

    answer = str(maxNumber)

    return answer

numbers = [3, 30, 34, 5, 9]

print(solution(numbers))