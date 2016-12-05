import redis
import zmq
import time

context = zmq.Context()
publisher = context.socket(zmq.PUB)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

publisher.bind("tcp://*:5563")

r.set("jsonMessage","")

while True:
    time.sleep(1)
    jsonMessage=r.get("jsonMessage")
    print jsonMessage
    maclist=r.lrange('maclist', 0, -1)
    print maclist
    if jsonMessage !="":
        r.set("jsonMessage","")
        r.delete("maclist")
        for mac in maclist:
            print mac
            r.delete("maclist")
            publisher.send_multipart([mac, jsonMessage])
        
    
