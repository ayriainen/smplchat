# smplchat

This project is a group work for master level course Distributed Systems at University of Helsinki. The main goal of this project is to design a large scale distributed system that has a global state, provides data consistensy and synchronization, has mechanisms for reaching consensus, is fault tolerant and scalable. The implementation of the designed system is done in small scale.

## Operation

Run in terminal from the project folder.

Install via:
```
poetry install
```

Run the app via:
```
poetry run smplchat
```

## Testing

You can test multiple clients on your own locally with Docker running.

In root, run:
```
docker build -t smplchat .
```
This will build an image but not start any containers yet.

Then in however many terminals with this command we start a container and also start the app in it:
```
docker run -it --rm smplchat
```

The image gets built with code changes but if you want to remove it run:
```
docker rmi smplchat
```
