import socket

def receive_image(save_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            with open(save_path, 'wb') as f:
                while (chunk := conn.recv(1024)):
                    f.write(chunk)
        print("Image received and saved.")

if __name__ == "__main__":
    receive_image('recieved_image.jpg', 'localhost', 65432)
