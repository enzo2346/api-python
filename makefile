.PHONY: run test docker package docker-run docker-push

HOST = '0.0.0.0'
PORT = '5000'
GITHUB_TOKEN = '<GITHUB_TOKEN>'
DOCKER_HUB_TOKEN = <DOCKER_HUB_TOKEN>

run:
	python -m src.main

test:
	coverage run -m unittest discover
	coverage report -m

package:
	pyinstaller --onefile --name api-python src/main.py

docker-run:
	docker build -t api-python .
	docker run -p ${PORT}:${PORT} -e HOST=${HOST} -e PORT=${PORT} -e GITHUB_TOKEN=${GITHUB_TOKEN} api-python

docker-push:
	docker login -u enzo2346 -p ${DOCKER_HUB_TOKEN}
	docker build -t api-python .
	docker tag api-python:latest enzo2346/api-python:latest
	docker push enzo2346/api-python:latest