# pip3 install web.py
# 
# Run this program like: python this.py 30801
# Usage: curl "http://localhost:30801/_PLACEHOLDER_APIKEY_/smsget"
# Usage: curl "http://localhost:30801/_PLACEHOLDER_APIKEY_/smsdel"
# Modified: no telegram notify

from usim800 import sim800
import sys

def sms_get_or_del(get_or_del):
    # Param: True for get, False for del
    # Return: message
    gsm = sim800(baudrate=9600,path="/dev/ttyUSB0")
    if get_or_del:
        res_dict = gsm.sms.readAll()
        result_str = ""
        if len(res_dict) == 0:
            result_str = "No SMS on this SIM."
        else:
            result_str = "SIM <b>17386011111</b><br />"
        for k in res_dict:
            num, sender, time, body = [res_dict[k][index] for index in [0,2,4,5]]
            result_str += '<b>{}</b> {} {} {}<br />'.format(num, sender, time, body)
        # with open('/tmp/debug', 'wb+') as f:
        #     f.write(result_str.encode("utf-8", "ignore"))
        return result_str[-4000:] # Max: 4096 chars
    else:
        gsm.sms.deleteAllReadMsg()
        return "Deleted all message on SIM"

def send_666_to_12306():
    gsm = sim800(baudrate=9600,path="/dev/ttyUSB0")
    print('Test send 666 to 12306...')
    gsm.sms.send('12306','666')

# import json,requests # callback: telegram api
# def telegram_notify(msg):
#     url = "https://maker.ifttt.com/trigger/recolxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#     payload = {
#         "value1": msg
#     }
#     headers = {
#         "Content-Type": "application/json"
#     }
#     requests.post(url, data=json.dumps(payload), headers=headers)

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, uri):
        if not uri.startswith('_PLACEHOLDER_APIKEY_'):
            return "Wrong API key"
        try:
            action = uri.split('/')[1].lower()
            if action == "smsget":
                get_or_del = True
            elif action == "smsdel":
                get_or_del = False
            elif action == "send12306":
                send_666_to_12306()
                return "Sent 666 to 12306, success"
            else:
                return "Wrong API usage. Expect smsget/smsdel"
            msg = sms_get_or_del(get_or_del)
            # telegram_notify(msg)
            return '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">' + "Done. Result:<br />" + msg
        except Exception as e:
            raise
            # return "API Error: " + str(e)

if __name__ == "__main__":
    app.run()


