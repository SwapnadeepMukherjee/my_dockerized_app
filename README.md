# my_dockerized_app

A small FastAPI service, containerized with Docker, with a CI pipeline that lints, tests, enforces a coverage threshold, and scans for security issues on every push.

## Overview

This repository is a minimal but real HTTP service: a FastAPI app exposing a health check and an info endpoint, packaged into a multi-stage Docker image running as a non-root user, with GitHub Actions enforcing code quality and security on every change.

It started as a hands-on practice project for Docker packaging and has grown into a small end-to-end example of production engineering practices: pinned dependencies, structured logging, environment-based configuration, automated testing with a coverage gate, and dependency/static-analysis security scanning in CI.

## Features

- FastAPI HTTP service with `/health` and `/info` endpoints
- Multi-stage Docker build: small runtime image, non-root user, pinned base image
- Structured JSON logging
- Environment-variable configuration (`PORT`, `LOG_LEVEL`, `APP_ENV`)
- CI pipeline (GitHub Actions): lint, tests with an enforced coverage threshold, dependency vulnerability scanning (`pip-audit`), static security analysis (`bandit`)

## Prerequisites

- [Python](https://www.python.org/) 3.11+ (for running locally without Docker)
- [Docker](https://www.docker.com/products/docker-desktop) (for running containerized)
- [Git](https://git-scm.com/) (optional, for cloning the repository)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/SwapnadeepMukherjee/my_dockerized_app.git
cd my_dockerized_app
```

### Run Locally (without Docker)

```bash
cd python-image
pip install -r requirements.txt
python app.py
```

The service starts on `http://localhost:8000`.

### Run with Docker

```bash
cd python-image
docker build -t my-python-app .
docker run -p 8000:8000 my-python-app
```

### Verify it's running

```bash
curl http://localhost:8000/health
```

## API

### `GET /health`

Liveness/readiness probe. Used by the Docker `HEALTHCHECK`.

```json
{"status": "ok"}
```

### `GET /info`

Basic runtime info.

```json
{"app_env": "development", "cwd": "/app"}
```

## Project Structure

```
my_dockerized_app/
├── LICENSE
├── README.md
├── .github/workflows/workflow.yml   # CI: lint, test+coverage, security scans
└── python-image/
    ├── Dockerfile                   # multi-stage build
    ├── requirements.txt
    ├── app.py                       # FastAPI service
    └── tests/
        ├── conftest.py
        └── test_app.py
```

## Configuration

The service reads configuration from environment variables at startup:

| Variable | Default | Description |
|---|---|---|
| `PORT` | `8000` | Port the server listens on |
| `LOG_LEVEL` | `INFO` | Python logging level (`DEBUG`, `INFO`, `WARNING`, ...) |
| `APP_ENV` | `development` | Environment name, returned by `/info` |

## Running Tests

```bash
cd python-image
pip install -r requirements.txt
pip install pytest pytest-cov httpx
pytest --cov=app --cov-fail-under=80
```

## CI/CD

On every push/PR to `main`, [GitHub Actions](.github/workflows/workflow.yml) runs: lint → tests with a coverage gate → dependency and static-analysis security scans.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Swapnadeep Mukherjee**

- GitHub: [@SwapnadeepMukherjee](https://github.com/SwapnadeepMukherjee)

## Support

If you encounter any issues or have questions, please open an [issue](https://github.com/SwapnadeepMukherjee/my_dockerized_app/issues) on the repository.

---
