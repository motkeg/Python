Write a simple centralized chat application.

Meaning you should write the server and the client.
The chat is centralized so all communication should go through him.

Two clients may connect each other using and API that you will design and write.

Stages:
1. Negotiation: 
	1.1 Each client will announce itself to the server. 
	1.2 The server will put the user in pending mode till another client will announce itself.
	1.3 Once the server has two clients he will introduce them (using your api).
2. Chat:
	2.1 The client will chat (may be random stuff) as they want.
	2.2 The server will print all communication.
	2.3 After the chat is over the clients may disconnect (using your api).
3. Folding:
	3.1 The disconnecting process should be clean (meaning using a API). Take TCP disconnection process as an example 
		(not needed to be this robust - you should assume you are using a reliable transport layer).
4. Bonus:
	4.1 Create a situation graph for the questions and answers. So the chat will be coherent and human understandable.
	4.2 Write a unitest for the server and the client.

You should two files: client.py and server.py. (and two more files if you are writing the bonus unitests).