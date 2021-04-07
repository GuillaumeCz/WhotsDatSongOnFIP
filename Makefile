
install:
	poetry install

lint:
	poetry run black --check .
	poetry run isort -c .
	poetry run flake8 .

lint-fix:
	poetry run black .
	poetry run isort .
