import zmq,threading

context = zmq.Context()
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

sock = context.socket(zmq.SUB)
sock.connect("tcp://localhost:6666")

name = input('请输入昵称：')

def receive():
    while True:
        sock.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
        resp = sock.recv().decode('utf-8')
        print(resp)


def write():
    while True:
        data = input('')
        socket.send_string(name+'：'+data)
        resplasd = socket.recv_string()
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()