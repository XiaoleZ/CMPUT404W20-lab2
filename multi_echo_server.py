#different func
#client: just create the socket connect to the server
#server: create the socket and find the host
import socket
import time
from multiprocessing import Process
HOST = ""
PORT = 8001
Buffer_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind((HOST,PORT)) 
        s.listen(2)
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            p = Process(target = handle_echo ,args=(addr,conn))
            p.daemon=True
            p.start()
            print("started process",s)
###
def handle_echo(addr, conn):
    print("connected by", addr)
    full_data =  conn.recv(Buffer_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    print(full_data)
    conn.close()


if __name__ =="__main__":
    main()