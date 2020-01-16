#different func
#client: just create the socket connect to the server
#server: create the socket and find the host
import socket
import time
HOST = ""
PORT = 8001
Buffer_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #question3 -reuse the same port
        s.bind((HOST,PORT)) 
        s.listen(2)
        while True:
            conn, adr = s.accept()
            print("Connected by", adr) #question4 - host & port
            ####
            full_data = conn.recv(Buffer_SIZE) #q5 -empty string is returned such as b"" 
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ =="__main__":
    main()