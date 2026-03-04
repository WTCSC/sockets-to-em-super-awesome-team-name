import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (replace with the server machine’s IP if needed)
client.connect((input("What is the host IP?\n"), int(input("What port?\n"))))
print("Connected to server")

# Send messages and receive responses
while 1==1:
    msg = input("Enter message: ")
    if not msg:
        break
    client.send(msg.encode())
    if msg.lower() == "goodbye":
      client.close()
      break
    response = client.recv(1024).decode()
    print(f"Server says: {response}")
