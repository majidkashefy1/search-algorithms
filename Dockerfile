# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy project
COPY . /app

# Install deps
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
