SHELL := /bin/bash

.PHONY: venv
venv: 
	python3 -m venv venv

.PHONY: activate
activate:
	source venv/bin/activate

.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: install
install: activate
	pip install -r requirements.txt

