#!make
include .env.local
export

run.db:
	docker compose -f docker-compose.local.yml up -d


db.down:
	docker compose -f docker-compose.local.yml down


migrate:
	python -m src.database.migrate


run:
	python -m src.main


run.test.db:
	@export $$(cat .env.test | xargs) && \
	docker compose -f docker-compose.test.yml up -d


test.db.down:
	docker compose -f docker-compose.test.yml down


migrate.test.db:
	@export $$(cat .env.test | xargs) && \
	python -m src.database.migrate


test:
	@export $$(cat .env.test | xargs) && \
	python -m pytest


test.endpoints:
	@export $$(cat .env.test | xargs) && \
	python -m pytest tests/api/test_lermontovizate_endpoints.py


test.service:
	@export $$(cat .env.test | xargs) && \
	python -m pytest tests/unit/services/test_lermontovization.py


test.repo:
	@export $$(cat .env.test | xargs) && \
	python -m pytest tests/integration/test_text_transformations_repo.py