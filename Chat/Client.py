from socket import AF_INET, SOCK_DGRAM, socket

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as c:
        while True:
            msg = input("Inserisci il messaggio: ")
            c.sendto(msg.encode(),("192.168.95.255",5000))

if __name__ == "__main__":
    chatClient()
