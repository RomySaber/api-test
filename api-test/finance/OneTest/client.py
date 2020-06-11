#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from socket import *

HOST ='192.168.15.247'

PORT = 7099

BUFFSIZE=2048

ADDR = (HOST,PORT)

tctimeClient = socket(AF_INET,SOCK_STREAM)

tctimeClient.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    tctimeClient.send(bytearray.fromhex(data))
    data = tctimeClient.recv(BUFFSIZE)
    if not data:
        break
    print('<' +''.join(format(x, '02x') for x in data))
tctimeClient.close()
