import socket

def send_file(filename, host, port):
    with open(filename, 'rb') as f:
        # Create socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to receiver
        s.connect((host, port))

        # Send file size to receiver
        filesize = len(f.read())
        s.sendall(str(filesize).encode())

        # Reset file cursor to beginning
        f.seek(0)

        # Send file to receiver
        s.sendfile(f)

        # Close socket connection
        s.close()
