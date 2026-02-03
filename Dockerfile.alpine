# syntax=docker/dockerfile:1.4
# Multi-stage Alpine build for a small and secure runtime image

########################################
# Builder stage: build wheels for caching
########################################
FROM python:3.13-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install build-time packages needed for compiling wheels
RUN apk add --no-cache \
    build-base \
    musl-dev \
    libffi-dev \
    openssl-dev \
    gcc

WORKDIR /app

# Copy dependency manifests first for better cache usage
COPY requirements/requirements.txt requirements/requirements-test.txt /app/requirements/

# Build wheels (if requirements.txt exists) to speed up subsequent installs
RUN python -m pip install --upgrade pip wheel setuptools \
    && if [ -f /app/requirements/requirements.txt ]; then pip wheel --wheel-dir /wheels -r /app/requirements/requirements.txt; fi

########################################
# Runtime stage: minimal Alpine image
########################################
FROM python:3.13-alpine AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:$PATH"

# Install minimal runtime packages (libraries) if native wheels require them
RUN apk add --no-cache \
    libffi \
    openssl

# Create a non-root user
RUN addgroup -S appuser && adduser -S -G appuser appuser

WORKDIR /app

# Copy prebuilt wheels from builder (if any) and install dependencies
COPY --from=builder /wheels /wheels
COPY requirements/requirements.txt /app/requirements/requirements.txt

RUN python -m pip install --upgrade pip \
    && if [ -d /wheels ] && [ "$(ls -A /wheels 2>/dev/null)" ]; then \
         pip install --no-index --find-links /wheels -r /app/requirements/requirements.txt; \
       else \
         pip install --no-cache-dir -r /app/requirements/requirements.txt; \
       fi \
    && rm -rf /wheels /root/.cache/pip

# Copy application sources (after deps so layer caching is effective)
COPY . /app

# Ensure app files are owned by non-root user
RUN chown -R appuser:appuser /app

USER appuser

# Run the CLI
ENTRYPOINT ["python3", "calcolatrice.py"]