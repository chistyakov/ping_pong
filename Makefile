.PHONY : up down logs restart tests format static_check build_prod build_dev

up :
	docker-compose up --build -d

down :
	docker-compose down

logs :
	docker-compose logs -f ${SERVICE}

attach:
	docker attach ${SERVICE} --detach-keys ctrl-c

restart :
	docker-compose restart ${SERVICE}

tests : build_dev
	docker run --rm --name tests ping_pong_dev tests

format : build_dev
	docker run --rm --name format -v ${PWD}:/app -u $$(id -u) ping_pong_dev format

static_check : build_dev
	docker run --rm --name format ping_pong_dev static_check

build_dev:
	docker build  --target dev --tag ping_pong_dev .
