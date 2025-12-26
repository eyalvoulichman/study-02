# Stage 1: Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies in a virtual environment to keep them isolated
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code
COPY app.py .

# Environment variables with defaults
ENV REDIS_HOST=redis-service
ENV REDIS_PORT=6379
ENV FLASK_APP=app.py

EXPOSE 8000

# Run the application
CMD ["python", "app.py"]

