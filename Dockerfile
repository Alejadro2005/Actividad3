# Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY main.py .
CMD ["python", "./main.py"]