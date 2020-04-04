import time
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

#Rounding
import time
now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))
