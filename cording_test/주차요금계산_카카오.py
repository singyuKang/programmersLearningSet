import math

def hourToMinutes(hours):
    h, m = map(int , hours.split(":"))
    return h*60+m

def solution(fees, records):
    answer = []
    dic = dict()
    #기본시간, 기본요금, 단위시간, 단위요금
    dt, df, ut, uf = fees
    
    for r in records:
        time, number, InOut = r.split()
        # print(time,number,InOut)
        number = int(number)
        if number in dic:
            dic[number].append([hourToMinutes(time), InOut])
        else:
            dic[number] = [[hourToMinutes(time), InOut]]
    myList = sorted(dic.items())
    # print(myList)
    for r in myList:
        t=0
        # print(r)
        
        for rr in r[1]:
            if(rr[1] == "IN"):
                t -= rr[0]
                
            elif(rr[1]=="OUT"):
                t += rr[0]
                
        if r[1][-1][1] =="IN":
            t += hourToMinutes("23:59")
            
        if t<= dt:
            answer.append(df)
        else:
            answer.append(df+math.ceil((t-dt)/ut)*uf)
            
    return answer
