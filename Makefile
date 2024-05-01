PROJECT_NAME="to_do_list_hex"

###
# Dependencies section
###
_base_pip:
	@pip install -U pip wheel poetry

_base_poetry:
	@poetry install

dev-dependencies: _base_pip _base_poetry ## Install development dependencies


###
# Lint section
###
_ruff:
	@ruff check .

_ruff-fix:
	@ruff check . --fix

_isort:
	@isort --diff --check-only src/

_black:
	@black --check src/

_isort-fix:
	@isort .

_black-fix:
	@black .

_dead_fixtures:
	@pytest --dead-fixtures src/

_mypy:
	@mypy src/

pre-commit:
	@pre-commit run --all-files

lint: _ruff _isort _black _mypy ## Run all linters
format: _isort-fix _black-fix _ruff-fix ## Format code


###
# Run section
###
run-dev: ## Run server with developement settings
	@uvicorn $(PROJECT_NAME).adapters.inbound.rest.main:app --host="0.0.0.0" --port=8000 --reload


###
# Migration section
###
create-db-migration: ## Create a new migration
	@alembic -c src/to_do_list_hex/adapters/outbound/db/alembic/alembic.ini revision --autogenerate -m "$(m)"

apply-db-migration: ## Apply the migration
	@alembic -c src/to_do_list_hex/adapters/outbound/db/alembic/alembic.ini upgrade head