import random
import socket
import struct

ip =socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
print (ip)