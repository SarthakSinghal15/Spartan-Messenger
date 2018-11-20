# Spartan-Messenger

The aim is to build a response-streaming RPC where the client sends a request to the server and gets a stream to read a sequence of messages back. The client reads from the returned stream until there are no more messages. As one can see in the example, one specifies a response-streaming method by placing the stream keyword before the response type. // Obtains the Features available within the given Rectangle. Results are // streamed rather than returned at once (e.g. in a response message with a // repeated field), as the rectangle may cover a large area and contain a // huge number of features.
```
rpc ReceiveMsg(Message) returns (stream Message) {} 
```
## Features

- Design group conversations among users. 
Run Spartan Server
```sh
python3 server.py
Spartan server started on port 3000.
```
Alice's Terminal
```sh
> python3 client.py alice
[Spartan] Connected to Spartan Server at port 3000.
[Spartan] User list: bob,charlie,eve,foo,bar,baz,qux
[alice] > Hey Bob!
[alice] >
```

Bob's Terminal
```sh
> python3 client.py bob
[Spartan] Connected to Spartan Server at port 3000.
[Spartan] User list: alice,charlie,eve,foo,bar,baz,qux
[alice] Hey Bob!
[bob] >
```

Bob's Terminal
```sh
...
[bob] > Hi Alice!
[bob] >
```

Alice's Terminal
```sh
...
[bob] Hi Alice!
[alice] >
```
- Implements a LRU Cache to store recent messages in memory. :floppy_disk: [2 points]
- Limit the number of messages a user can send to an API within a time window e.g., 15 requests per second. NOTE: The rate limiting should work for a distributed setup. :vertical_traffic_light: [1 point]


- Provided end-to-end message encryption using [AES from PyCrypto library](https://docs.python-guide.org/scenarios/crypto/#pycrypto). :key:
- Added [Decorator](https://www.python-course.eu/python3_decorators.php) for the LRU cache (E.g @lru_cache) and rate limition (E.g. @rate). :cyclone:

- Extend your design to support group chats. :family:

## App Config

- Used config.yaml to load users for the Spartan messenger.
