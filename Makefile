.PHONY: start-docker-app
start-docker-app:
	COMPOSE_FILE=docker-compose.yml docker compose up -d

.PHONY: start-docker-dbs
start-docker-dbs:
	COMPOSE_FILE=docker-compose-dbs.yml docker compose up -d 