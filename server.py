import socket
import threading
import random

lock = threading.Lock()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = {}

def broadcast(message, sender_conn=None):
    with lock:
        dead = []
        for client in clients:
            if client != sender_conn:
                try:
                    client.sendall(message)
                except Exception as e:
                    print("Removing dead client:", e)
                    dead.append(client)

        for client in dead:
            client.close()
            del clients[client]

def handle_client(conn, addr):
    print(f"Connected to {addr}")
    username = ""
    conn.send("\nEnter username: ".encode())
    while username == "":
      print("Getting username...")
      username = conn.recv(1024).decode().strip()
    print("Recieved username!")
    with lock:
      clients[conn] = username
    broadcast(f"\n{clients[conn]} has joined the chat.\n".encode(), conn)
    print("Broadcasting to:", list(clients.values()))
    while True:
      try:
          msg = conn.recv(1024)

          # Client disconnected
          if not msg:
              print(f"{clients[conn]} disconnected.")
              with lock:
                  del clients[conn]
              conn.close()
              broadcast(f"{clients[conn]} has left the chat.\n".encode())
              break

          msg = msg.decode()
          print(f"Received: {msg}")

          if msg.lower() == "goodbye":
              print(f"{clients[conn]} has left the chat")
              with lock:
                  del clients[conn]
              conn.close()
              broadcast(f"{clients[conn]} has left the chat.\n".encode())
              break

          broadcast(f"\n{clients[conn]} said: {msg}\n".encode(), conn)

      except Exception as e:
          print("Error:", e)
          break

# Bind to 0.0.0.0:5000
servport = random.randrange(5000, 12000, 1)
server.bind((input("input your server's ip: "), servport))
print(f"10.103.0.70 : {servport}")

# Listen for connections
server.listen(10)
print("Waiting for connection...")

while True:
    conn, addr = server.accept()  # NEW socket per client
    threading.Thread(target=handle_client, args=(conn, addr)).start()
