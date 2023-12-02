from usim800 import sim800
import sys
gsm = sim800(baudrate=9600,path="/dev/ttyUSB0")

if len(sys.argv) == 2 and sys.argv[1] == 'del':
    print('Deleting all msg...')
    gsm.sms.deleteAllReadMsg()
else:
    print('Reading all msg...')
    res_dict = gsm.sms.readAll()
    for k in res_dict:
        print(res_dict[k])

