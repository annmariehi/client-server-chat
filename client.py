# Programming Project 4: Client/Server Chat
# client.py

import socket

def client():
    # SOURCE FOR FOLLOWING SOCKET SET UP:
    # Date: 08/10/22
    # Adapted from function at:
    # URL: https://realpython.com/python-sockets/

    # define host/port/socket
    HOST = socket.gethostname()
    PORT = 3000
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set up socket on client side
    clientsocket.connect((HOST, PORT)) # connect to server

    # first message prompt
    print('type /q to quit\nenter message to send...')

    # SOURCE FOR FOLLOWING WHILE LOOP:
    # Date: 08/10/22
    # Adapted from function at:
    # URL: https://realpython.com/python-sockets/
    while True:
        message = input('>> ')

        # if user inputs '/q', terminate connection
        if(message == '/q'):
            print('terminating connection...')
            break

        # send the message
        clientsocket.send(message.encode())

        # receive server message
        recvMessage = clientsocket.recv(1024).decode()

        # if server terminated connection, will receive nothing and close socket
        if not recvMessage:
            print('...server terminated connection.')
            break

        # print server message
        print(f's: {recvMessage}')

    # if broken out of while loop, close connection with server
    clientsocket.close()


if __name__ == '__main__':
    client()
