# SETUP
.PHONY: setup
setup:
	pip install -r requirements.txt

# CHECK
.PHONY: lint
lint:
	mypy lelang
	pylint lelang
	flake8 lelang


# DOCKER
.PHONY: compose-up
compose-up:
	docker compose up -d

.PHONY: compose-down
compose-down:
	docker compose down

.PHONY: compose-rs
compose-rs:
	make compose-down
	make compose-up

# MIGRATIONS
.PHONY: make-migrations
make-migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

# lelang
.PHONY: run
run:
	python manage.py runserver

.PHONY: run-full
run-full:
	make compose-up
	sleep(5)
	make migrate
	make run


