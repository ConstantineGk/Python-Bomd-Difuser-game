import socket
import sys
import time
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.27"
port = 8888
try:
    soc.connect((host, port))
except:
    print("Connection error")
def main():
    try:
        soc.recv(5120).decode('utf8')
    except:
        print('Connection Error')
        sys.exit()
    while True:
        try:
            soc.sendall('timer'.encode('utf8'))
            time.sleep(1)
        except:
            print('Connection Error')
            break
if __name__ == "__main__":
   main()    
