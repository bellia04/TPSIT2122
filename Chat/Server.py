from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 4096

HOST = "0.0.0.0"
PORT = 5000


def chatServer():
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Server in ascolto')
        while running == True:
            msg = s.recvfrom(BUFFER_SIZE)
            msg = msg[0].decode()
            mex = msg.split(',')
            msg = '>>' + mex[0] + ': ' + mex[1]
            print(msg)

if __name__ == "__main__":
    chatServer()