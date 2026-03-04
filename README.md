# sockets-to-em-super-awesome-team-name

> 🚀 A simple multiclient chat application built with Python sockets and
> threading.

This project demonstrates a basic TCP chat system where multiple clients
can connect to a server, send messages, and receive broadcasts from
other connected users.

------------------------------------------------------------------------

## 📌 Features

-   Multi-client support\
-   Username prompt on connection\
-   Message broadcasting to all connected users\
-   Graceful client disconnect handling\
-   Threaded communication (simultaneous send/receive)

------------------------------------------------------------------------

## 🛠 Requirements

-   Python 3.x\
-   No external libraries required (uses built-in `socket` and
    `threading`)

Check your Python version:

``` bash
python3 --version
```

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── server.py   # Chat server
    ├── client.py   # Chat client
    └── README.md   # Project documentation

------------------------------------------------------------------------

## 🚀 How to Run

### 1️⃣ Start the Server

On the host machine:

``` bash
python server.py
```

The server will start listening and display the IP address and port.

------------------------------------------------------------------------

### 2️⃣ Connect a Client

On the same machine or another device on the network:

``` bash
python client.py
```

When prompted:

    What is the host IP?

Enter the server's IP address.

    What port?

Enter the port number shown by the server.

------------------------------------------------------------------------

## 💬 How to Use

-   Enter a username when prompted.\
-   Type messages and press Enter to send.\
-   All connected users will receive broadcasted messages.\
-   Type:

```{=html}
<!-- -->
```
    goodbye

to disconnect cleanly.

------------------------------------------------------------------------

## ⚙️ How It Works

### Server

-   Creates a TCP socket\
-   Accepts incoming client connections\
-   Prompts for and stores usernames\
-   Uses threads to handle multiple clients simultaneously\
-   Broadcasts received messages to all connected clients

### Client

-   Connects to the server via IP and port\
-   Runs a receiving thread to listen for incoming messages\
-   Sends user input to the server

------------------------------------------------------------------------

## 🧪 Testing

To test broadcasting:

1.  Start the server\
2.  Open multiple terminals\
3.  Connect multiple clients\
4.  Send messages from different clients and observe broadcasts

------------------------------------------------------------------------

## 🐛 Troubleshooting

**Connection Refused** - Make sure the server is running\
- Verify the IP and port\
- Check firewall/network settings

**Messages Not Appearing** - Ensure the receiving thread is running\
- Confirm clients are successfully connected

------------------------------------------------------------------------

## 📚 Educational Purpose

This project was created as a networking/socket programming exercise to
demonstrate real-time communication using TCP.

------------------------------------------------------------------------

## ✨ Future Improvements

-   Private messaging\
-   GUI client\
-   Persistent chat history\
-   Encryption (SSL/TLS)\
-   Nickname change support
