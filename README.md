# my_dockerized_app

Build and run a Python app in a Docker container.

## Overview

This repository contains a Python application packaged and containerized using Docker. It demonstrates how to build, configure, and run a Python application within a Docker container for consistent development, testing, and deployment environments.

## Features

- 🐳 Docker containerization for easy deployment
- 🐍 Python-based application
- 📦 Reproducible environments across different systems
- 🚀 Simple setup and execution

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop) (latest version)
- [Git](https://git-scm.com/) (optional, for cloning the repository)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/SwapnadeepMukherjee/my_dockerized_app.git
cd my_dockerized_app
```

### Build the Docker Image

Navigate to the `python-image` directory and build the Docker image:

```bash
cd python-image
docker build -t my-python-app .
```

### Run the Container

To run the containerized application:

```bash
docker run my-python-app
```

## Project Structure

```
my_dockerized_app/
├── README.md                 # This file
├── .gitattributes           # Git configuration
├── .github/                 # GitHub configuration (workflows, templates, etc.)
└── python-image/            # Docker image definition
    └── Dockerfile           # Docker configuration for Python app
```

## Configuration

### Docker Build Arguments

You can customize the build by passing build arguments:

```bash
docker build -t my-python-app --build-arg PYTHON_VERSION=3.9 python-image/
```

### Environment Variables

Configure the application by setting environment variables when running the container:

```bash
docker run -e VAR_NAME=value my-python-app
```

## Usage

Detailed usage instructions can be found in the `python-image/` directory.

## Development

To make changes to the application:

1. Modify the source files in the `python-image/` directory
2. Rebuild the Docker image:
   ```bash
   docker build -t my-python-app python-image/
   ```
3. Test the changes by running the container

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License (or specify your license).

## Author

**Swapnadeep Mukherjee**

- GitHub: [@SwapnadeepMukherjee](https://github.com/SwapnadeepMukherjee)

## Support

If you encounter any issues or have questions, please open an [issue](https://github.com/SwapnadeepMukherjee/my_dockerized_app/issues) on the repository.

---
