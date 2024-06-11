.PHONY: up down restart restartweb restartdb
.SILENT:

up:
	- docker compose -f docker-compose.yml up --build -d

down:
	- docker compose -f docker-compose.yml down

restart:
	- docker compose -f docker-compose.yml down
	- docker compose -f docker-compose.yml up -d

restartweb:
	- docker compose -f docker-compose.yml down web
	- docker compose -f docker-compose.yml up web -d

restartdb:
	- docker compose -f docker-compose.yml down db
	- docker compose -f docker-compose.yml up db -d