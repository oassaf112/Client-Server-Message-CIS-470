# This code demonstrates a simple client-server interaction -> -> ->
# -> ->over a secure connection using the RSA encryption algorithm.

import socket  # import the socket module to handle network communication
import rsa  # import the RSA encryption algorithm library
import threading  # import threading to handle concurrent processing
import os  # import the operating system module to terminate the program

# Generate RSA keys for the client
public_key_client, private_key_client = rsa.newkeys(1024)

# Initialize the server's public key to None
public_key_server = None

# Set the server's address and port
server_address = "localhost"
server_port = 80

# Create a TCP/IP socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server
client.connect((server_address, server_port))

# Print a message to indicate that the client has connected to the server
print("Connected to server at port", server_port)
print("Server address:", server_address)

# Receive the server's public key and save it to public_key_server
public_key_server = rsa.PublicKey.load_pkcs1(client.recv(1024))

# Send the client's public key to the server
client.send(public_key_client.save_pkcs1("PEM"))

# Print a message to indicate that the client has received the server's public key
print("\nPublic key received.")


# Define a function to send messages from the client to the server
def send_message(c):
    while True:
        # Prompt the user to enter a message
        print("\nPlease type a message: ")
        message = input("")

        # Check if the message is blank
        if message == "":
            print("\nMessage cannot be blank.")
            continue

        # Check if the user wants to exit the program
        if message == "exit":
            client.close()
            print("\nDisconnected from server.")
            os._exit(1)

        # Encrypt the message using the server's public key and send it to the server
        else:
            encrypted = rsa.encrypt(message.encode(), public_key_server)
            c.send(encrypted)
            print("\nClient: " + message)
            print("\nClient (Encrypted): \n" + str(encrypted, errors="ignore"))


# Define a function to receive messages from the server
def receive_message(c):
    while True:
        try:
            # Decrypt the message using the client's private key and print it to the console
            received = rsa.decrypt(c.recv(1024), private_key_client).decode()
            print("\nServer: " + rsa.decrypt(c.recv(1024), private_key_client).decode())
            print("\nServer (Encrypted): \n" + str(received, errors="ignore"))
            print("\nPlease type a message: ")

        # If an error occurs, print a message and exit the program
        except:
            print("\nThe server has closed.")
            os._exit(1)


# Create threads to handle sending and receiving messages concurrently
send_thread = threading.Thread(target=send_message, args=(client,)).start()
receive_thread = threading.Thread(target=receive_message, args=(client,)).start()
