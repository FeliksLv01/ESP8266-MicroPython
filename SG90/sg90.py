import machine
import time

#设置PWM 引脚G5,频率50Hz
servo = machine.PWM(machine.Pin(5), freq=50)
servo.duty(75)  #舵机角度的设定 25 0度
#125  180度
time.sleep_ms(500)
servo.duty(40)
time.sleep_ms(500)
servo.duty(100)
time.sleep_ms(500)
servo.duty(75)
time.sleep_ms(500)
