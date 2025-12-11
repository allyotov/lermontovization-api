#!make
include .env
export

run:
	python -m src.main

test:
	python -m pytest

migrate:
	python -m src.database.migrate