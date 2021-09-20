import time
from adafruit_servokit import ServoKit

import os
import subprocess

p = subprocess.Popen(['i2cdetect', '-y','1'],stdout=subprocess.PIPE,) 
#cmdout = str(p.communicate())

for i in range(0,9):
    line = str(p.stdout.readline())
    print(line)

# kit1 = Servokit(channels=16, address = 0*41)
# 
# kit1.servo[0].angle = 180
# kit1.servo[1].angle = 180
# kit1.servo[2].angle = 180
# kit1.servo[3].angle = 180
# time.sleep(2)
# 
# kit1.servo[0].angle = 0
# kit1.servo[1].angle = 0
# kit1.servo[2].angle = 0
# kit1.servo[3].angle = 0
# time.sleep(2)
# 
# kit.servo[0].angle = 90
# kit.servo[1].angle = 90
# kit.servo[2].angle = 90
# kit.servo[3].angle = 90



