import redis
import zmq
import time
import base64
import threading
import json


r = redis.StrictRedis(host='localhost', port=6379, db=0)
#connect zmq for mac list
context = zmq.Context()
context1 = zmq.Context()
sock = context1.socket(zmq.REP)
sock.bind("tcp://*:5564")
###def func for thread
def worker():
    with open("jsonlist.json", "r+") as f:
        jsonlist = json.loads(f.read())
    while True:
        mac = sock.recv()
        if mac not in jsonlist:
            jsonlist.append(mac)
        with open('jsonlist.json', 'w') as outfile:
           json.dump(jsonlist, outfile)
        sock.send("recived")

t = threading.Thread(target=worker)
t.start()

#connect zmq for pubish
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5563")

r.set("jsonMessage","")
r.delete("maclist")


def send_textmessage():
    maclist=r.lrange('maclist', 0, -1)
    r.set("jsonMessage","")
    r.delete("maclist")
    for mac in maclist:
        r.delete("maclist")
        publisher.send_multipart([mac.strip(), jsonMessage])


def send_voicemessage():
    maclist=r.lrange('maclist', 0, -1)
    with open("media/Speaker/voice/"+voicename+".wav", "rb") as voicefile:
            encoded_string = base64.b64encode(voicefile.read())
    r.set("voicename","")
    r.delete("maclist")
    for mac in maclist:
        print mac
        r.delete("maclist")
        publisher.send_multipart([mac.strip(), encoded_string])


while True:
    time.sleep(1)
    jsonMessage = r.get("jsonMessage")
    voicename = r.get("voicename")
    if jsonMessage != "":
        send_textmessage()
    if voicename != "":
        send_voicemessage()
        


