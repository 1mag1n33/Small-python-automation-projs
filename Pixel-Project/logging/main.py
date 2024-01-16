import socket

pc_ip = 'localhost'  # Replace with your PC's IP address
pc_port = 5000 # Replace with the same port used in your Flask app

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((pc_ip, pc_port))
    s.listen()

    print(f"Listening for connections on {pc_ip}:{pc_port}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode('utf-8')
        print(f"Received data: {data}")