#from multiprocessing import Pool
import socket, time

HOST = ""
PORT = 8001
Buffer_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    s.sendall(payload.encode())
    s.shutdown(socket.SHUT_WR)

    full_data = s.recv(Buffer_SIZE)
    '''
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(Buffer_SIZE)
    
    except Exception as e:
        print(e)
    finally:
        s.close()
    '''
def main():
    address = (('127.0.0.1',8001))
    connect(address)
    '''
    with Pool() as p:
        p.map(connect, address*10)
    '''


if __name__ =="__main__":
    main()