from typing import Any

from fastapi import FastAPI

app = FastAPI(
    title="AI Starter API",
    description="A comprehensive Python starter template for AI/ML projects",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/", response_model=dict[str, str])
def root() -> dict[str, str]:
    """Root endpoint that returns a welcome message."""
    return {"message": "Hello AI Expert!"}


@app.get("/health", response_model=dict[str, str])
def health_check() -> dict[str, str]:
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}


@app.get("/info", response_model=dict[str, Any])
def app_info() -> dict[str, Any]:
    """Application information endpoint."""
    return {
        "name": "AI Starter",
        "version": "0.1.0",
        "description": "A comprehensive Python starter template for AI/ML projects",
        "docs": "/docs",
        "redoc": "/redoc",
    }


def main() -> None:
    """Main function for running the application."""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
