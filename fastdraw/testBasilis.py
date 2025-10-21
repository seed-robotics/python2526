import time
import random

print("Get ready")
randomTime = random.randint(1,5)
time.sleep(randomTime)
print("draw")
startTime = time.time()
input()
pushTime = time.time()-startTime  
i=round(pushTime,4)
if pushTime<0.1:
    print("Loser, reaction time was", i)
elif pushTime>0.3:
    print("Loser, reaction time was", i)  
else:
    print("well done, reaction time was",i)

