import random
import time 

print("get ready")
randomTime = random.randint (1,5)
time.sleep(randomTime)
print("draw")
pushTime=time.time()
input()
reactionTime =  time.time() - pushTime

if reactionTime < 0.15:
    print("you are too fast!",round(reactionTime,2), "s")
elif reactionTime > 0.3:
    print("you are too slow!",round(reactionTime,2), "s")
else:
    print("you did it!") 
    print("reaction time was",round(reactionTime,2), "s")