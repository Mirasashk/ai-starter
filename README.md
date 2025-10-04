# AI Starter

A comprehensive Python starter template for AI/ML projects with FastAPI backend, modern tooling, and best practices.

## 🚀 Features

-   **FastAPI Backend**: Modern, fast web framework for building APIs
-   **AI/ML Stack**: Pre-configured with popular libraries including:
    -   PyTorch for deep learning
    -   Transformers for NLP
    -   Scikit-learn for traditional ML
    -   LangChain for LLM applications
    -   MLflow for experiment tracking
-   **Modern Python**: Uses `pyproject.toml` for configuration (PEP 518/621 compliant)
-   **Code Quality**: Pre-commit hooks with Black, Ruff, isort, and mypy
-   **Testing**: Pytest setup with coverage reporting and comprehensive test suite
-   **CI/CD**: GitHub Actions workflow for automated testing
-   **Development Tools**: Streamlined Makefile with common development commands
-   **Containerization**: Docker and Docker Compose for development and production
-   **Type Safety**: Full type hints and mypy static type checking
-   **Documentation**: Auto-generated API docs and comprehensive README
-   **Environment Management**: Direnv support for automatic virtual environment activation

## 📦 Dependencies

This project includes a comprehensive set of AI/ML and web development dependencies:

### Core Framework

-   `fastapi` - Modern web framework for APIs
-   `uvicorn` - ASGI server
-   `pydantic` - Data validation
-   `gunicorn` - WSGI server for production

### AI/ML Libraries

-   `torch`, `torchvision`, `torchaudio` - PyTorch ecosystem
-   `transformers` - Hugging Face transformers
-   `datasets` - Hugging Face datasets
-   `accelerate` - Accelerate training
-   `sentence-transformers` - Sentence embeddings
-   `langchain` - LLM application framework
-   `mlflow` - ML lifecycle management
-   `scikit-learn` - Traditional ML algorithms
-   `faiss-cpu` - Vector similarity search

### Data Science

-   `numpy` - Numerical computing
-   `pandas` - Data manipulation
-   `matplotlib` - Data visualization

### Development & Testing

-   `pytest` - Testing framework
-   `pytest-cov` - Coverage reporting
-   `pytest-asyncio` - Async testing support
-   `httpx` - HTTP client for testing
-   `black` - Code formatting
-   `ruff` - Fast linter
-   `isort` - Import sorting
-   `mypy` - Static type checking
-   `pre-commit` - Git hooks
-   `joblib` - Model serialization

## 🛠️ Setup

### Prerequisites

-   Python 3.11+
-   pip

### Installation

1. **Clone the repository**

    ```bash
    git clone <repository-url>
    cd ai-starter
    ```

2. **Quick setup** (recommended)

    ```bash
    make setup
    ```

    This will install all dependencies and set up pre-commit hooks.

3. **Manual setup** (alternative)

    ```bash
    # Install production dependencies
    pip install -e .

    # Or install with development dependencies
    pip install -e ".[dev,test]"

    # Set up pre-commit hooks
    pre-commit install
    ```

4. **Virtual environment setup** (isolated environment)

    ```bash
    # Create virtual environment
    python3 -m venv .venv

    # Activate virtual environment
    source .venv/bin/activate

    # Install dependencies
    pip install -e ".[dev,test]"

    # Set up pre-commit hooks
    pre-commit install
    ```

5. **Automatic activation with direnv** (optional but recommended)

    ```bash
    # Install direnv (if not already installed)
    curl -sfL https://direnv.net/install.sh | bash

    # Add to your shell configuration
    echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
    source ~/.bashrc

    # Allow direnv for this project
    direnv allow .

    # Now the virtual environment will activate automatically when you cd into the project
    ```

## 🚀 Usage

### Virtual Environment

**With direnv (automatic activation):**

```bash
# Just navigate to the project directory
cd /home/miras/ai/ai-starter

# Virtual environment activates automatically!
# You can verify with: echo $VIRTUAL_ENV
```

**Without direnv (manual activation):**

```bash
# Activate virtual environment
source .venv/bin/activate

# Your prompt should show (.venv) indicating the virtual environment is active
# You can verify with: echo $VIRTUAL_ENV

# To deactivate when done
deactivate
```

### Running the FastAPI Server

**Development server:**

```bash
make run
# or
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

**Production server:**

```bash
make run-prod
# or
gunicorn src.app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Docker development environment:**

```bash
make docker-dev
# or
docker-compose up --build
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:

-   **Interactive API docs**: `http://localhost:8000/docs`
-   **ReDoc documentation**: `http://localhost:8000/redoc`
-   **Health check**: `http://localhost:8000/health`
-   **App info**: `http://localhost:8000/info`

### Testing

Run the test suite:

```bash
make test
# or
pytest
```

Run with coverage:

```bash
make test-cov
# or
pytest --cov=src --cov-report=html --cov-report=term-missing
```

Run all quality checks:

```bash
make ci
```

### Jupyter Notebooks

Start Jupyter for experimentation:

```bash
# Using Docker (recommended)
make docker-dev
# Then access http://localhost:8888

# Or install jupyter locally
pip install jupyter
jupyter notebook notebooks/
```

## 🛠️ Available Commands

This project includes a comprehensive `Makefile` with common development commands:

### Setup & Installation

```bash
make setup          # Complete development setup
make install        # Install production dependencies
make install-dev    # Install development dependencies
```

### Development

```bash
make run            # Start FastAPI development server
make run-prod       # Start production server
make docker-dev     # Start Docker Compose development environment
```

### Testing & Quality

```bash
make test           # Run tests
make test-cov       # Run tests with coverage
make test-watch     # Run tests in watch mode
make lint           # Run linting (ruff + mypy)
make format         # Format code (black + isort + ruff)
make format-check   # Check code formatting
make ci             # Run full CI pipeline locally
```

### Docker

```bash
make docker-build   # Build Docker image
make docker-run     # Run Docker container
```

### Utilities

```bash
make clean          # Clean build artifacts
make help           # Show all available commands
```

## 📁 Project Structure

```
ai-starter/
├── src/
│   └── app.py              # FastAPI application with health checks
├── tests/
│   ├── test_app.py         # Comprehensive API tests
│   └── conftest.py         # Pytest fixtures and configuration
├── notebooks/
│   └── 01_getting_started.ipynb  # Example ML workflow notebook
├── data/                   # Data directory (gitignored)
│   └── .gitkeep
├── models/                 # Models directory (gitignored)
│   └── .gitkeep
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD
├── pyproject.toml          # Modern Python project configuration
├── Makefile               # Development commands
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Multi-service development environment
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .envrc                 # Direnv configuration for automatic venv activation
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔧 Development

### Code Quality

This project uses several tools to maintain code quality:

-   **Black**: Automatic code formatting
-   **Ruff**: Fast Python linter
-   **isort**: Import statement sorting
-   **mypy**: Static type checking
-   **Pre-commit**: Git hooks for code quality

All tools are configured to run automatically on commit when pre-commit is installed.

**Quick commands:**

```bash
# Format code
make format

# Check formatting
make format-check

# Run linting
make lint

# Run all quality checks
make ci
```

### Adding New Dependencies

1. Add the package to `pyproject.toml` in the appropriate section (`dependencies` or `[project.optional-dependencies]`)
2. Install it: `pip install -e ".[dev,test]"` (for dev dependencies) or `pip install -e .` (for core dependencies)
3. Update this README if it's a significant addition

### Adding New Features

1. Create new modules in the `src/` directory
2. Add corresponding tests in the `tests/` directory
3. Update the FastAPI app in `src/app.py` to include new endpoints
4. Follow the existing code style and patterns
5. Run tests: `make test`

## 🚀 Deployment

### Docker (Recommended)

**Build and run with Docker:**

```bash
# Build the image
make docker-build
# or
docker build -t ai-starter:latest .

# Run the container
make docker-run
# or
docker run -p 8000:8000 ai-starter:latest
```

**Development with Docker Compose:**

```bash
# Start all services (FastAPI + Jupyter + MLflow)
make docker-dev
# or
docker-compose up --build
```

This starts:

-   FastAPI app at `http://localhost:8000`
-   Jupyter notebook at `http://localhost:8888`
-   MLflow tracking at `http://localhost:5000`

**Production Dockerfile:**

The included `Dockerfile` is production-ready with:

-   Python 3.11 slim base image
-   Non-root user for security
-   Health checks
-   Optimized for production

### Cloud Deployment

This application can be deployed to various cloud platforms:

-   **Heroku**: Use the included `gunicorn` configuration
-   **AWS**: Deploy using AWS Lambda with Mangum adapter
-   **Google Cloud**: Use Cloud Run or App Engine
-   **Azure**: Deploy to Azure Container Instances or App Service

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run quality checks: `make ci`
5. Run tests: `make test`
6. Commit your changes: `git commit -m "Add feature"`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

**Development workflow:**

```bash
# Set up development environment
make setup

# Make your changes, then run quality checks
make ci

# Run tests
make test

# Format code if needed
make format
```

## 📝 License

[Add your license information here]

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 📚 Getting Started

### Example Workflow

The `notebooks/01_getting_started.ipynb` notebook demonstrates:

1. **API Testing**: How to test your FastAPI endpoints
2. **Data Processing**: Loading and exploring data with pandas
3. **Model Training**: Training a scikit-learn model
4. **Model Evaluation**: Metrics, confusion matrix, and feature importance
5. **Model Persistence**: Saving models and results
6. **Integration**: Connecting notebooks with your FastAPI backend

### Quick Start Example

```python
# Test your API
import requests
response = requests.get("http://localhost:8000/health")
print(response.json())  # {'status': 'healthy'}

# Train a simple model
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, random_state=42)
model = RandomForestClassifier()
model.fit(X, y)
print(f"Model accuracy: {model.score(X, y):.3f}")
```

## 🔗 Useful Links

-   [FastAPI Documentation](https://fastapi.tiangolo.com/)
-   [PyTorch Documentation](https://pytorch.org/docs/)
-   [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
-   [LangChain Documentation](https://python.langchain.com/)
-   [MLflow Documentation](https://mlflow.org/docs/)
-   [Scikit-learn Documentation](https://scikit-learn.org/stable/)
-   [Pytest Documentation](https://docs.pytest.org/)
-   [Docker Documentation](https://docs.docker.com/)
