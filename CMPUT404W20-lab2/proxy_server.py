import socket, time, sys
#from multiprocessing import Process

HOST = ""
PORT = 8001
Buffer_SIZE = 1024
def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()
    return remote_ip
'''
def handle_request(conn, addr, proxy_end):
    send_full_data = conn.recv(Buffer_SIZE)
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(Buffer_SIZE)
    conn.send(data)
'''
def main():
    host = "www.google.com"
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #question3 -reuse the same port
        proxy_start.bind((HOST,PORT)) 
        proxy_start.listen(1)
        while True:
            conn, adr = proxy_start.accept()
            print("connected by", adr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("connecting to google")
                remote_ip= get_remote_ip(host)

                proxy_end.connect((host,port))
                #####
                #p = Process(traget = handle_request)
                #####
                send_full_data = conn.recv(Buffer_SIZE)
                print("sending recieved data "+send_full_data.decode('utf-8')+ "to google")
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(Buffer_SIZE)
                print("sending recieved data"+data.decode('utf-8')+ " to client")
                conn.send(data)
                ####

            conn.close()

if __name__ == "__main__":
    main()