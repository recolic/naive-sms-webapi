# naive sms HTTP API

A naive API server to remote-access your SMS without phone!

This is a very naive API server, to remote-access your SMS. Warning: it doesn't even support parallel requests. For personal use only.

## requires

[SIM800C USB to GSM module](https://www.amazon.com/EC-Buying-Quad-Band-Integrated-Transmission/dp/B0B64X81LD/ref=sr_1_4?crid=2KW2A16T3C6R0&keywords=sim800&qid=1701559081&sprefix=sim800%2Caps%2C350&sr=8-4)

python3

python usim800 module (please clone from github: <https://github.com/Bhagyarsh/usim800> . pip release is too old)

## how to use

### step 1 - test if your SIM800 module is working

Run `python pullsms.py`. If it prints your SMS correctly, you are good.

### step 2 - start api server

Run `python apiserver.py 8080` as daemon.

### step 3 - enjoy

Try if your api server is working.

```
curl "http://localhost:8080/mO0c7JlqE1n5r/smsget"
curl "http://localhost:8080/mO0c7JlqE1n5r/smsdel"
```





