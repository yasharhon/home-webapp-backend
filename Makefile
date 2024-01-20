make-image:
	sudo docker build --target tornado-server -t tornado-server-image .

start-server:
	sudo docker run -p 8888:8888 --rm -t tornado-server-image:latest python main.py
