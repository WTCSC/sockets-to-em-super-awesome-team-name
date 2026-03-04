import socket
import threading

# Create a socket object
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (replace with the server machine’s IP if needed)
conn.connect((input("What is the host IP?\n"), int(input("What port?\n"))))
print("Connected to server")

def recieving(conn):
    while True:
      received = conn.recv(1024).decode()
      if received != "" and received != "*blank*":
        print(received)

threading.Thread(target=recieving, args=(conn,)).start()

# Send messages and receive responses
while True:
    msg = input()
    if not msg:
        msg = "*blank*"
    conn.send(msg.encode())
    if msg.lower() == "goodbye":
      conn.close()
      quit()
