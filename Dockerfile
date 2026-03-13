FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip show gunicorn > /dev/null 2>&1 || pip install gunicorn


COPY . .


EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3 \
    CMD curl -f http://localhost:8080/docs || exit 1



CMD ["gunicorn", "-w", "2","-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind=0.0.0.0:8000"]
