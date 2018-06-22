#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from Crypto.PublicKey import RSA

#public= open('public_key.pem','r').read()
#public = RSA.importKey(public)

private = open("private_key.pem","r").read()
private = RSA.importKey(private)
public_key=private.publickey()
r="rec"

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1',4045))
serversocket.listen(1)

(client_server,address) = serversocket.accept()

client_server.send(public_key.exportKey())
x=client_server.recv(2048)

if r in x:
	data= x.replace(r,'')
	decrypt = eval(data)
	decryption=private.decrypt(decrypt)
	print decryption

