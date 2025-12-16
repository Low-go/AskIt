FROM python:3.11-slim

WORKDIR /app

RUN pip install uv
COPY requirements.txt .
RUN uv venv && \
    . .venv/bin/activate && \
    uv pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/bash", "-c", ". .venv/bin/activate && ./setup_dev.sh"]