.PHONY: up down restart restartweb restartdb init base addons test modules tests
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

init:
	- docker exec web-odoo bash -c "curl 'localhost:8069/web/database/create' --data 'master_pwd=admin_password&name=odoo14&login=odoo&password=odoo&phone=123456&lang=en_US&country_code=id&demo=0' --compressed"

base:
	- docker exec web-odoo bash -c "odoo --stop-after-init -d odoo14 -u all"

addons:
	- docker exec web-odoo bash -c "odoo --stop-after-init -d odoo14 -i supplier,material"

test:
	- docker exec web-odoo bash -c "odoo --test-enable --stop-after-init -d odoo14 -u supplier,material"

modules:
	- make base && make addons && make restartweb

tests:
	- make test && make restartweb