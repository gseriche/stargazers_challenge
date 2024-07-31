# GitHub Stars Counter

This project fetches the star count for specified GitHub repositories and outputs the results in YAML format. It demonstrates creating a simple Python program with unit tests, packaging it as a Docker image, and setting up a CI/CD pipeline with GitHub Actions.

## Features

- Fetch star counts for GitHub repositories
- Output results in YAML format
- Packaged as a Docker image
- CI/CD pipeline with GitHub Actions
- Unit tests

## Prerequisites

- Docker installed on your machine
- Git (optional, for cloning the repository)

## Usage

### Running with Docker

1. Pull the Docker image:

   ```bash
   docker pull gseriche/stargazers_challenge:latest
   ```

2. Run the Docker container:

   ```bash
   docker run --rm gseriche/stargazers_challenge:latest
   ```

This will fetch the star counts for the default repositories (vscode, cpython, django) and display the results.

### Customizing Repositories

To fetch star counts for different repositories, you can override the default command:

```bash
docker run --rm gseriche/stargazers_challenge:latest python main.py "owner1/repo1" "owner2/repo2"
```

Replace "owner1/repo1" and "owner2/repo2" with the GitHub repositories you're interested in.

## Development

### Setting Up the Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/gseriche/stargazers_challenge.git
   cd stargazers_challenge
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Run the unit tests with:

```bash
python -m unittest test_main.py
```

### Building the Docker Image Locally

Build the Docker image:

```bash
docker build --platform linux/amd64 -t stargazers_challenge:local .
```

Run the locally built image:

```bash
docker run --rm stargazers_challenge:local
```

## CI/CD Pipeline

This project uses GitHub Actions for its CI/CD pipeline. The workflow does the following:

1. Runs unit tests on pull requests and pushes to the main branch.
2. Builds and pushes a Docker image to Docker Hub when a new tag is pushed.

### Secrets Management

The CI/CD pipeline uses GitHub Secrets to securely manage sensitive information:

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: A Docker Hub access token (not your password)

These secrets are used in the GitHub Actions workflow for authenticating with Docker Hub.

## Technical Demonstrations

1. **Simple Program with Unit Tests**: The `main.py` file contains the main program, and `test_main.py` contains the unit tests.

2. **OCI/Docker Image**: The project includes a Dockerfile for building a container image.

3. **CI/CD Pipeline**: The `.github/workflows/ci-cd.yml` file defines the GitHub Actions workflow for continuous integration and deployment.

4. **Responsible Handling of Secrets**: Sensitive information is managed using GitHub Secrets, demonstrating secure practices for handling credentials.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
