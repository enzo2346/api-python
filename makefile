.PHONY: run test docker

run:
	python -m src.main

test:
	coverage run -m unittest discover
	coverage report -m

docker:
	docker build -t flask-app .
	docker run -d -v .:/app -p 8080:8080 flask-app python -m src.main
