# Ops-Status

Ops-Status is an evolving FastAPI service for monitoring the availability and response time of selected services.

The project is also an end-to-end DevOps learning environment: application development, containerization, automated testing, CI/CD, Kubernetes deployment, infrastructure as code, and observability will be added through working milestones.

> **Project status:** Early development. The local application, container workflow, and first external service check are working. The broader delivery roadmap remains in progress.

## Current Capabilities

- FastAPI application with `/` and `/health` endpoints
- Timed external HTTP check through `/checks`
- Reachability, HTTP status, and latency reporting
- Environment-based target configuration
- Docker image based on `python:3.12-slim`
- Non-root container execution
- Reproducible local startup with Docker Compose
- Machine-specific configuration excluded from source control

## Current Stack

- Python
- FastAPI
- Uvicorn
- HTTPX
- Docker
- Docker Compose

## Quick Start

### Requirements

- Docker Engine
- Docker Compose plugin

### Run the application

Copy the example configuration:

```bash
cp .env.example .env
```

Edit `.env` for the service you want Ops-Status to check, then build and start the container:

```bash
docker compose up -d --build
```

Confirm that the application is running:

```bash
docker compose ps
```

Test the application health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Run the configured external service check:

```bash
curl http://127.0.0.1:8000/checks
```

Stop the application:

```bash
docker compose down
```

## Configuration

Docker Compose reads local values from `.env` and passes the required application configuration into the container.

| Variable | Purpose |
|---|---|
| `OPS_STATUS_TARGET_NAME` | Display name for the monitored service |
| `OPS_STATUS_TARGET_URL` | URL requested by the monitoring check |
| `OPS_STATUS_TARGET_HOSTNAME` | Hostname used for the local container DNS override |
| `OPS_STATUS_TARGET_IP` | IP address mapped to the target hostname |

The real `.env` file is ignored by Git. `.env.example` documents the required variables using safe example values.

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Basic application information |
| `/health` | Confirms that Ops-Status itself is responding |
| `/checks` | Runs the configured external service check |

Example `/checks` response:

```json
{
  "name": "grafana",
  "reachable": true,
  "status_code": 302,
  "latency_ms": 46.9
}
```

A redirect such as HTTP `302` can still represent a successful reachability check. It confirms that the target responded even though it did not return HTTP `200`.

## Roadmap

- [x] FastAPI application foundation
- [x] Docker image and non-root execution
- [x] Docker Compose workflow
- [x] First timed external service check
- [x] Environment-based target configuration
- [ ] Multiple monitored services
- [ ] Automated unit and integration tests
- [ ] GitHub Actions CI/CD
- [ ] k3s staging deployment
- [ ] Prometheus metrics and Grafana dashboards
- [ ] Floci-based AWS integration testing
- [ ] Terraform-managed AWS deployment
- [ ] Controlled release and rollback workflow

## Project Direction

The immediate goal is to turn the working single-service prototype into a configurable, tested monitoring foundation. Later milestones will promote the same versioned application through local development, k3s staging, and a controlled AWS production environment.