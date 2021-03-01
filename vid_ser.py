#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import socket
import cv2
import pickle
import struct
import imutils
import cv2

async def sender(frame):
    await websocket.send(frame, binary=False)
    
def time(websocket, path):

    while True:
        print("hi1")

        camera = True
        if camera == True:

            vid = cv2.VideoCapture(0)
        else:
            vid = cv2.VideoCapture('videos/video1.mp4')
        try:
            while(vid.isOpened()):
                
                img, frame = vid.read()
                frame = imutils.resize(frame, width=320)
                a = pickle.dumps(frame)
                #message = struct.pack("Q", len(a))+a
                #await websocket.send(frame, binary=True)
                sender("hi")
                #print("sent frame")
        except :
            print("hi3")

            
            pass
                
start_server = websockets.serve(time, "127.0.0.1", 9999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
