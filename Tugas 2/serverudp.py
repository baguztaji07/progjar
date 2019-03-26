import socket
import select

HOST = "127.0.0.1"
PORT = 5005
timeout = 3
imagecounter = 1
basename = "new_%s"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print "File name:", data
        file_name = data.strip()

    f = open(basename % file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(40960000)
            f.write(data)
        else:
            print "%s Finish!" % file_name
            f.close()
            break