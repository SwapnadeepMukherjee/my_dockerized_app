FROM python:3.11-slim

RUN useradd --create-home --uid 1000 appuser
WORKDIR /app

COPY --chown=appuser:appuser . .

USER appuser

CMD ["python3", "app.py"]