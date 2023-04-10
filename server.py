import tkinter as tk
import socket
import sys
import traceback
from threading import Thread
import os
class Initial:
    def __init__(self,root):
        self.p=root
        label=tk.Label(root,text=socket.gethostbyname(socket.gethostname()),font='Arial 50')
        label.pack(expand=1,fill='both')
        button=tk.Button(root,text='Close',font='Arial 20',bg='light blue', width=30,command=self.f2)
        button.pack(expand=0)
    def f2(self):
        global text
        self.p.destroy()
def start():
    w=tk.Tk()
    w.geometry('600x200')
    w.title('Server IP Address')
    myapp=Initial(w)
    w.mainloop()


def main():
    start_server()


def start_server():
    global cl
    host = socket.gethostbyname(socket.gethostname())
    port = 8888         # arbitrary non-privileged port

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(3)       # queue up to 2 requests
    print("Socket now listening")
    # infinite loop- do not reset for every requests
    l=[]
    cl=[]
    
    thread1=Thread(target=start).start()
    thread2=Thread(target=timing).start()
    while True:
        
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)
        l.append(ip)
        l.append(port)
        cl+=[connection]
        if len(l)==6:
            try:
                for c in cl:
                    t1=Thread(target=client_thread, args=(c, ip, port)).start()
            except:
                print("Thread did not start.")
            
        
    soc.close()
def client_thread(connection, ip, port):
    is_active=True
    while is_active:
        try:
            client_input=receive_input(connection)
        except:
            print('Client not connected.')
            break
        if 'wrong' in client_input:
            dat='wrong'
        if 'fine' in client_input:
            dat='0'
        if '1.sc1' in client_input:
            dat='Player1 sc1.1'
        if '1.sc2' in client_input:
            dat='Player1 sc2.1'
        if '1.sc3' in client_input:
            dat='Player1 sc3.1'
        if '1.sc4' in client_input:
            dat='Player1 sc4.1'
        if '1.sc5' in client_input:
            dat='Player1 sc5.1'
        if '1.sc6' in client_input:
            dat='Player1 sc6.1'
        if '1.sc7' in client_input:
            dat='Player1 sc7.1'
        if '1.sc8' in client_input:
            dat='Player1 sc8.1'
        if '1.sc9' in client_input:
            dat='Player1 sc9.1'
        if '1.sc10' in client_input:
            dat='Player1 sc10.1'
        if '1.sc11' in client_input:
            dat='Player1 sc11.1'
        if '2.sc1' in client_input:
            dat='Player2 sc1.2'
        if '2.sc2' in client_input:
            dat='Player2 sc2.2'
        if '2.sc3' in client_input:
            dat='Player2 sc3.2'
        if '2.sc4' in client_input:
            dat='Player2 sc4.2'
        if '2.sc5' in client_input:
            dat='Player2 sc5.2'
        if '2.sc6' in client_input:
            dat='Player2 sc6.2'
        if '2.sc7' in client_input:
            dat='Player2 sc7.2'
        if '2.sc8' in client_input:
            dat='Player2 sc8.2'
        if '2.sc9' in client_input:
            dat='Player2 sc9.2'
        if '2.sc10' in client_input:
            dat='Player2 sc10.2'
        if '2.sc11' in client_input:
            dat='Player2 sc11.2'
        if '2.sc12' in client_input:
            dat='Player2 sc12.2'
        if '2.sc13' in client_input:
            dat='Player2 sc13.2'
        if '2.sc14' in client_input:
            dat='Player2 sc14.2'
        if '2.sc15' in client_input:
            dat='Player2 sc15.2'
        if '2.sc16' in client_input:
            dat='Player2 sc16.2'
        if '2.sc17' in client_input:
            dat='Player2 sc17.2'
        if '2.sc18' in client_input:
            dat='Player2 sc18.2'
        if '2.sc19' in client_input:
            dat='Player2 sc19.2'
        if 'cable' in client_input:
            dat='wcable'
        if 'done1' in client_input:
            dat='Player1 done1'
        if 'done2' in client_input:
            dat='Player2 done2'
        if 'timer' in client_input:
            dat='timer'
        for c in cl:
            try:
                c.send(dat.encode("utf8"))
            except:
                print('Client not connected.')
                break
def receive_input(connection):
    client_input=connection.recv(1024)
    decoded_input = client_input.decode("utf8").rstrip()
    result = process_input(decoded_input)
    return result
def process_input(input_str):
    x=input_str
    return x

def timing():
    import socket
    import sys
    import time
    soc =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 8888
    try:
        soc.connect((host, port))
    except:
        print('Connection Error')
    try:
        data=soc.recv(5120).decode('utf8')
    except:
        print('Connection Error')
    while True:
        try:
            soc.sendall('timer'.encode('utf8'))
            time.sleep(1)
        except:
            #print('Connection Error')
            break
    
 
if __name__ == "__main__":
   main()

