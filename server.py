import zmq,threading
 
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

sock = context.socket(zmq.PUB)
sock.bind("tcp://*:6666")

def handle():
    while True:
        message = socket.recv_string()
        print(message)
        sock.send_string(message)
        socket.send_string(message)

thread = threading.Thread(target=handle)
thread.start()