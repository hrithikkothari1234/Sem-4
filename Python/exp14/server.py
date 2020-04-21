import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((socket.gethostname(), 7765))

print("__SERVER__ side...")

while True:
    data, address=s.recvfrom(1024)

    print('->>>receiver says :', str(data))

    msg = input('SERVER : ')

    s.sendto(bytes(msg, 'utf-8'), address)
    print('sent')
    