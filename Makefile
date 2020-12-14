.PHONY : service_a service_b tests format static_check build_prod build_dev

service_a : build_prod
	docker run --rm --name service_a -it --publish 5001:5001 ping_pong_prod service_a

service_b : build_prod
	docker run --rm --name service_b -it --publish 5002:5002 ping_pong_prod service_b

tests : build_dev
	docker run --rm --name tests ping_pong_dev tests

format : build_dev
	docker run --rm --name format -v ${PWD}:/app -u $$(id -u) ping_pong_dev format

static_check : build_dev
	docker run --rm --name format ping_pong_dev static_check

build_prod:
	docker build  --target prod --tag ping_pong_prod .

build_dev:
	docker build  --target dev --tag ping_pong_dev .
