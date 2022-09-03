#!/usr/bin/env python
# coding: utf-8
import random
# In[1]:


import random


# In[5]:


random.randint(1,50)


# In[7]:


for i in range(10):
    print(random.randint(1,50))


# In[ ]:


usernum =int(input("Enter a number between 1 to 50 - "))


# In[ ]:


import random
def guessNum():
    
    playagain='y'
    
    while playagain == 'y'
        score=0
        sysNum= random.randint(1,50)
        userNum= int(input("Enter a number between 1 to 50 - "))
        diff = sysNum-userNum
        if diff==0:
            print("Wow you're great you have guessed it right..!!")
            score+=50
            print("Your score is boosted", score)
        elif diff>=-5 and diff<=5:
            print("you are very close to the number")
            print("userNum = ", userNum)
            print("sysNum =", sysNum)
            score+=25
            print("Your score is boosted", score)
        elif diff>=-10 and diff<=10:
            print("you are close to the number")
            print("userNum = ", userNum)
            print("sysNum =", sysNum)
            score+=10
            print("Your score is boosted", score)
        else:
            print("sorry you didn't make it")
            print("userNum = ", userNum)
            print("sysNum =", sysNum)
            print("your final score is - ", score)
            
        playagain = input("\nDo you want to play again 'y/n'")
    else:
        print("your final score is - ", score)


# In[ ]:


guessNum()


# In[ ]:




