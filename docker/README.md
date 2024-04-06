# docker image for sms-remote-access

```
docker build -t recolic/sms --build-arg R_SEC_HMSAPI_KEY=$R_SEC_HMSAPI_KEY .

docker run -d --restart always --log-opt max-size=10M --name rsms     --device=/dev/ttyUSB0 -p 30801:30801 recolic/sms
```



