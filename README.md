In this project, you are required to develop a simple Web server in ANY programming language that is capable of processing only one request. 
Functions:
1.	Specifically, your Web server will (i) create a connection socket when contacted by a client (browser); (ii) receive the HTTP request from this connection; (iii) parse the request to determine the specific file being requested; (iv) get the requested file from the server’s file system; (v) create an HTTP response message consisting of the requested file preceded by header lines; and (vi) send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present in your server, your server should return a “404 Not Found” error message.  (50 points)
2.	You are required to send text messages from one client to another client via the server. The text messages must be encrypted during the transmission and decrypted when they reach another client. The related information of encryption, decryption, and the transmission via the server must be printed out. The encryption and decryption are required to use RSA. The integrity of each message should be check to ensure there is no lost/tampered information during the transmission.  (50 points)
3.	You are required to provide codes for the client side of this service to enable file sharing between clients. The server will keep a list of all the files that each client has for querying purpose.  The functionality of the server is introduced here to provide you the necessary information to implement the correct client side of the service. The server stores names and keywords of all the files that clients share. When a client tries to lookup files associated with a specific keyword, the server will retrieve this information from the stored .txt file and send to the requested client. To transfer the requested file, the client should send one file-type message. However, to receive the requested file, the client should keep calling receive until the total length of bytes are received. Keywords: The client side should have a file directory storing shared files and one keyword.txt file contains all keywords. The format of the keyword file is: key1, filename1; key2, filename2; key3, filename1; … … . Each file can have multiple keywords, and each keyword can be associated with multiple files. (25 bonus points)
4.	You are required to make your program process multiple requests (sending and receiving text messages) at the same time. (25 bonus points)

Test:
After you finish the web server, you should run following test to verify its correctness.
1.  start server.
2.  start sending text messages between two clients
3.  clientA joins the server, then sends messages to the server, and waits for another client
5.  clientB joins the server, and receives the related messages from the server 
6.  clientA and clientB build the connection 
7. clientB and sends an acknowledgement for each received message to clientA via the server
8. the integrity of each message should be check to ensure there is no lost/tampered information during the transmission  
9. repeat until all the text messages are successfully transmitted

Sample Python codes:
Python codes: sending and receive messages

https://stackoverflow.com/questions/57664539/how-to-send-and-receive-messages-between-client-and-server-in-python

https://www.geeksforgeeks.org/python-program-that-sends-and-recieves-message-from-client/

RSA encryption and decryption:
https://www.kite.com/python/answers/how-to-encrypt-and-decrypt-a-message-with-rsa-in-python

