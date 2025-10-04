.PHONY: help install install-dev setup test test-cov test-watch lint format format-check clean run run-prod build docker-build docker-run docker-dev ci

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Setup & Installation
install: ## Install production dependencies
	pip install -e .

install-dev: ## Install development dependencies
	pip install -e ".[dev,test]"

setup: install-dev ## Complete development setup
	pre-commit install
	@echo "✅ Development environment setup complete!"
	@echo "Run 'make run' to start the FastAPI server"
	@echo "Run 'make test' to run tests"
	@echo "Run 'make format' to format code"

# Development
run: ## Start FastAPI development server
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Start production server
	gunicorn src.app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Testing & Quality
test: ## Run tests
	pytest -q --maxfail=1 --disable-warnings

test-cov: ## Run tests with coverage
	pytest --cov=src --cov-report=html --cov-report=term-missing

test-watch: ## Run tests in watch mode
	pytest-watch -- -q --maxfail=1

lint: ## Run linting (ruff + mypy)
	ruff check src tests
	mypy src

format: ## Format code (black + isort + ruff --fix)
	black src tests
	isort src tests
	ruff check --fix src tests

format-check: ## Check code formatting
	black --check src tests
	isort --check-only src tests
	ruff check src tests

ci: format-check lint test ## Run full CI pipeline locally

# Docker
docker-build: ## Build Docker image
	docker build -t ai-starter:latest .

docker-run: ## Run Docker container
	docker run -p 8000:8000 ai-starter:latest

docker-dev: ## Start Docker Compose development environment
	docker-compose up --build

# Build
build: ## Build the package
	python -m build

# Utilities
clean: ## Clean build artifacts and caches
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .coverage htmlcov/
	rm -rf .mypy_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
