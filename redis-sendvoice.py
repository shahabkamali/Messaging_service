import redis
import zmq
import time
import base64

context = zmq.Context()
publisher = context.socket(zmq.PUB)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

publisher.bind("tcp://*:5563")

r.set("voicename","")
r.delete("maclist")

while True:
    time.sleep(1)
    voicename=r.get("voicename")
    print voicename
    maclist=r.lrange('maclist', 0, -1)
    print maclist
    if voicename !="":
        with open("media/Speaker/voice/"+voicename+".wav", "rb") as voicefile:
            encoded_string = base64.b64encode(voicefile.read())
        r.set("voicename","")
        r.delete("maclist")
        for mac in maclist:
            print mac
            r.delete("maclist")
            publisher.send_multipart([mac.strip(), encoded_string])
        
    
