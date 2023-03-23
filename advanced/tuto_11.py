#CH 8 225
import sys
sys.path.append('.')
import importlib
import tuto_10
importlib.reload(tuto_10)

# slots

#MODULE PACKAGING TUTORIAL PYPY TEST AND PYPY PROD
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

#CH 9 247 I/O
# BYTEARRAYS
bts=bytes([0x65,0x66])
bytex=bytearray()
bytex.extend(b'world')
a=b'hello'
a.decode('utf-8')
#CH 10 USEFUL STANDARD LIBRARY
# https://docs.python.org/3/library/
# collections
# itertools
# unittest
# statistics
# shutil
# datetime
# time
# os
# re
# socket
# inspect
# sys
# pathlib and path
# math
#io


#COMMAND LINE LIBS
import argparse

def main(argv):
    p = argparse.ArgumentParser(description="This is some program")
    # A positional argument
    p.add_argument("infile")
    # An option taking an argument
    p.add_argument("-o","--output", action="store")
    # An option that sets a Boolean flag
    p.add_argument("-d","--debug", action="store_true", default=False)
    # Parse the command line
    args = p.parse_args(args=argv)
    # Retrieve the option settings
    infile = args.infile
    output = args.output
    debugmode = args.debug
    print(infile, output, debugmode)


#ENV VARIABLE
import os,socket
# path = os.environ['PATH']
# user = os.environ['USERS']
OS = os.environ['OS']
USER = os.environ['TEMP'].split('\\')
HNAME=socket.gethostname()
IP=socket.gethostbyname(HNAME)
print(OS,IP,USER[2],HNAME)



#buffer

#object serialization
#encoding json/xml
import pickle,json
obj={'data':{'type':12}}
# cd=pickle.dumps(obj)
cd=json.dumps(obj)
# print(pickle.loads(cd))
print(json.loads(cd))

#block operations an dconcurrency
import socket
#blocking setter
# sock.setblocking(False)
# #block
# data = sock.recv(8192)
#io polling
# from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
# def run(sock1, sock2):
# selector = DefaultSelector()
# selector.register(sock1, EVENT_READ, data=reader1)
# selector.register(sock2, EVENT_READ, data=reader2)
# # Wait for something to happen
# while True:
# for key, evt in selector.select():
# func = key.data
# func(key.fileobj)


#THREADS
# import threading
# t1 = threading.Thread(target=reader1, args=[sock1])
# t1.start()

# # Wait for the threads to finish
# t1.join()

#CONCURRENCY WITH ASYNCIO

# import asyncio
# async def reader1(sock):
# loop = asyncio.get_event_loop()
# while (data := await loop.sock_recv(sock, 8192)):
# print('reader1 got:', data)
# async def reader2(sock):
# loop = asyncio.get_event_loop()
# while (data := await loop.sock_recv(sock, 8192)):
# print('reader2 got:', data)
# async def main(sock1, sock2):
# loop = asyncio.get_event_loop()
# t1 = loop.create_task(reader1(sock1))
# t2 = loop.create_task(reader2(sock2))
# # Wait for the tasks to finish
# await t1
# await t2
# ...
# # Run it
# asyncio.run(main(sock1, sock2))



#mstsc or ssh ip
# if __name__ == '__main__':
#     import sys
#     main(sys.argv[1:])
