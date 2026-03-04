import socket
import threading

lock = threading.Lock()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = {}

def broadcast(message, sender_conn=None):
    with lock:
        for client in list(clients.keys()):
            if client != sender_conn:
                try:
                    client.sendall(message)
                except:
                    client.close()
                    del clients[client]

def handle_client(conn, addr):
    print(f"Connected to {addr}")
    conn.sendall("Enter username: ".encode())
    username = conn.recv(1024).decode().strip()
    with lock:
      clients[conn] = username
    broadcast(f"{clients[conn]} has joined the chat.\n".encode(), conn)
    while True:
      msg = conn.recv(1024).decode()
      if not msg:
          msg = "*blank*"
      print(f"Received: {msg}")
      if msg.lower() == "goodbye":
        print(f"{clients[conn]} has left the chat")
        with lock:
          del clients[conn]
        conn.close()
        break
      try:
        conn.send(f"Server received: {msg}".encode())
        broadcast(f"{clients[conn]} said: {msg}".encode(), conn)
      except:
        print("Connection broken")
        break

# Bind to 0.0.0.0:5000
server.bind(("0.0.0.0", 6769))

# Listen for connections
server.listen(1)
print("Waiting for connection...")

while True:
    conn, addr = server.accept()  # NEW socket per client
    threading.Thread(target=handle_client, args=(conn, addr)).start()
