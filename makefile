.PHONY: run test docker package docker-run docker-push

HOST = '0.0.0.0'
PORT = '5000'
GITHUB_TOKEN = '<GITHUB_TOKEN>'
TAG = V1

run:
	python -m src.main

test:
	coverage run -m unittest discover
	coverage report -m

package:
	pyinstaller --onefile --name simple-flask-app src/main.py

docker-run:
	docker build -t simple-flask-app .
	docker run -p ${PORT}:${PORT} -e HOST=${HOST} -e PORT=${PORT} -e GITHUB_TOKEN=${GITHUB_TOKEN} simple-flask-app

docker-push:
	docker build -t simple-flask-app:${TAG} .
	docker tag simple-flask-app:${TAG} enzo2346/simple-flask-app:${TAG}
	docker push enzo2346/simple-flask-app:${TAG}