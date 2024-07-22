import socket

def send_image(image_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(image_path, 'rb') as f:
            while (chunk := f.read(1024)):
                s.sendall(chunk)
    print("Image sent.")

if __name__ == "__main__":
    send_image('green.jpg', 'localhost', 65432)
