#!/usr/bin/env python
# coding: utf-8

# In[26]:


def solution(participant, completion):
    answer = ''
    completion.sort()
    participant.sort()
    print(participant)
    print(completion)

    for index in range(len(participant)):
            if completion[index] != participant[index]:
                return participant[index]
            elif(index == len(participant)):
                return participant[-1]
                
            
                
        

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant,completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant,completion))

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant,completion))


# In[ ]:




