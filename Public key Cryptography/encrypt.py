#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from Crypto.PublicKey import RSA


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 4045))

rec=s.recv(2048)
ser_public_key = RSA.importKey(rec)

msg = open('asn1.txt', 'r')
x=msg.read()
msg.close()
print x 

enc=ser_public_key.encrypt(x,32)
s.send("rec"+ str(enc))
print str(enc)

s.close()

