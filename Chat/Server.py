from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024
HOST = "0.0.0.0"
PORT = 5000
var = True

def chatServer():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST,PORT))
        while var == True:
            msg = s.recvfrom(BUFFER_SIZE)
            print(msg[0].decode())

if __name__ == "__main__":
    chatServer()