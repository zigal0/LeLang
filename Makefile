# LeLang
.PHONY: run
run:
	python manage.py runserver


.PHONY: make-migrations
make-migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

# SETUP
.PHONY: setup
setup:
	pip install -r requirements.txt

# CHECK
.PHONY: lint
lint:
	mypy --strict lelang
	pylint lelang
	flake8 lelang

.PHONY: test
test:
	pytest # --cov

.PHONY: check
check:
	make test
	make lint

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


