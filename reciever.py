import socket

def receive_file(filename, port):
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to port
    s.bind(('0.0.0.0', port))

    # Listen for incoming connections
    s.listen(1)

    # Accept incoming connection
    conn, addr = s.accept()

    # Receive file size from sender
    filesize = int(conn.recv(1024).decode())

    # Receive file from sender
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    # Close socket connection
    conn.close()
    s.close()
