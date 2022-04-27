def solution(s):
    answer = s
    number_dic = {
        "zero":"0",
        "one" :"1",
        "two" :"2",
        "three" :"3",
        "four" :"4",
        "five" :"5",
        "six" :"6",
        "seven" :"7",
        "eight" :"8",
        "nine" :"9",
    }
    myList = ""
    for key, value in number_dic.items():
        print(key, value)
        answer = answer.replace(key, value)

    # print(number_dic["eight"])
    st = ""
    for c in s:
        if(c.isdigit()):
            myList += c
        else:
            if(st in number_dic):
                myList += str(number_dic[st])
                st=""
            else:
                st+=c
        if(st in number_dic):
            myList +=str(number_dic[st])
            st=""
            

                
    # print(myList)
    answer = int(myList)
    return answer
