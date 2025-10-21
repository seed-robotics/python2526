import random, sys, time 

print('Fast Draw')
print()
print('Time to test your reflexes and see if you are the fastest\ndraw in the west!')

print('When you see "DRAW", you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
input('Press Enter to begin...')

while True:
    print('It is high noon...')
    
    print('DRAW!')
    drawTime = time.time()
    input()  # This function call doesn't return until Enter is pressed.
    timeElapsed = time.time() - ?

    if timeElapsed < ?:
        print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed > ?:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw.')
        print('You are the fastest draw in the west! You win!')

    print('Enter QUIT to stop, or press Enter to play again.')
