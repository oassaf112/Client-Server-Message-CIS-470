import socket
import rsa
import threading
import os

# Generate a new RSA key pair for the server
public_key_server, private_key_server = rsa.newkeys(1024)

# Initialize the client's public key as None
public_key_client = None

# Set up the server's address and port
server_address = "localhost"
server_port = 80

# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server.bind((server_address, server_port))

# Listen for incoming connections
server.listen(1)

# Print a message to indicate that the server is ready and waiting for a client to connect
print("Server ready at port", server_port)
print("Server address:", server_address)
print("Waiting for client to connect...")

# Accept an incoming connection from a client
client, _ = server.accept()
print("\nClient connected.")

# Send the server's public key to the client
client.send(public_key_server.save_pkcs1("PEM"))

# Receive the client's public key
public_key_client = rsa.PublicKey.load_pkcs1(client.recv(1024))

print("\nPublic key received.")


# Define a function to send messages from the server to the client
def send_message(c):
    while True:
        print("\nPlease type a message: ")
        message = input("")

        if message == "":
            print("\nMessage cannot be blank.")
            continue

        if message == "exit":
            server.close()
            print("\nServer closed.")
            os._exit(1)

        else:
            encrypted = rsa.encrypt(message.encode(), public_key_client)
            c.send(encrypted)
            print("\nServer: " + message)
            print("\nServer (Encrypted): \n" + str(encrypted, errors="ignore"))


# Define a function to receive messages from the client
def receive_message(c):
    while True:
        try:
            print("\nClient: " + rsa.decrypt(c.recv(1024), private_key_server).decode())
            print("\nPlease type a message: ")

        except:
            print("\nClient disconnected. The server will now close.")
            os._exit(1)


# Create a thread to run the send_message function
send_thread = threading.Thread(target=send_message, args=(client,)).start()

# Create a thread to run the receive_message function
receive_thread = threading.Thread(target=receive_message, args=(client,)).start()
