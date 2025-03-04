.PHONY: build test check

build:
	python3 app.py

test:
	python3 -m unittest discover -s tests

check:
	pyright .
