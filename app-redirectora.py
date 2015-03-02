#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Cada vez que os conectéis al servidor,
 debe aparecer en el navegador Hola. Dame otra'',
 dondeDame otra'' es un enlace a una URL aleatoria bajo
 \verb|localhost:1234|
 (esto es, por ejemplo, \url{http://localhost:1234/324324234}).
 Esa URL ha de ser distinta cada vez que un navegador se conecte a la aplicación.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        numrandom = random.randint (0, 1000000)
        recvSocket.send("HTTP/1.1 301 Moved Permanently\r\n\r\n" +                        
                        "<html>"
                        "<head>"
                        "<META http-equiv='refresh' content='0;URL="+ str(numrandom)+"'/>"
                        "</head>" 
                        "<body><h1>Pagina aleatoria</h1>" + str(numrandom) + "</body></html>"            
                        "\r\n")                        
                        
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()