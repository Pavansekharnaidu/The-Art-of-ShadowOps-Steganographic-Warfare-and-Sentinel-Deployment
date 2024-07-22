import socket

def receive_image(save_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()                                                      # Listen for incoming connections
        conn, addr = s.accept()                                         # Accept a connection request from a client
        with conn:                                                      
            print(f"Connected by {addr}")
            with open(save_path, 'wb') as f:
                while (chunk := conn.recv(1024)):                       #recieving chunks from alice
                    f.write(chunk)                                      #writing in the file       
        print("Image received and saved.")                              

if __name__ == "__main__":
    receive_image('recieved_image.jpg', 'localhost', 65432)             #calling function
