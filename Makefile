.PHONY : up down logs tests format static_check build_prod build_dev

up :
	docker-compose up --build -d

down :
	docker-compose down

logs :
	docker-compose logs -f

tests : build_dev
	docker run --rm --name tests ping_pong_dev tests

format : build_dev
	docker run --rm --name format -v ${PWD}:/app -u $$(id -u) ping_pong_dev format

static_check : build_dev
	docker run --rm --name format ping_pong_dev static_check

build_dev:
	docker build  --target dev --tag ping_pong_dev .
