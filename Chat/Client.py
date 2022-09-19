from socket import AF_INET, SOCK_DGRAM, socket

PORT = 5000

def chatClient():
    running = True
    nome = input("Inserire il nome utente: ")
    ip = input("Inserisci l'indirizzo ip: ")
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            msg = input("Inserire il messaggio: ")
            if msg == 'exit' or msg == 'EXIT':
                running = False
            else:
                msg = nome + ',' + msg + ',' + ip + ',' + str(PORT)
                msg = msg.encode()
                s.sendto(msg, ("192.168.1.255", PORT))


if __name__ == "__main__":
    chatClient()
