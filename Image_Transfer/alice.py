import socket

def send_image(image_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))                             # Connect to the specified host and port
        with open(image_path, 'rb') as f:                   # file opening
            while (chunk := f.read(1024)):                           
                s.sendall(chunk)                            # sending chunks of 1024 bytes
    print("Image sent.")

if __name__ == "__main__":
    send_image('green.jpg', 'localhost', 65432)             # calling function
