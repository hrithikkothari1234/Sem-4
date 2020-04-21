import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("__CLIENT__ side...")

while True:
    msg = input('CLIENT : ')
    client_socket.sendto(msg.encode('utf-8'), (socket.gethostname(), 7765))
    print('sent')

    data, address = client_socket.recvfrom(1024)
    print('--> server says :')

    print(str(data))
    client_socket.sendto(bytes(msg, 'utf-8'), address)
    print('sent')
    