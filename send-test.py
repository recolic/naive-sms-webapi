from usim800 import sim800
import sys
gsm = sim800(baudrate=9600,path="/dev/ttyUSB0")

print('Test send 666 to 12306...')
gsm.sms.send('12306','666')

