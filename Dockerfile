FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential gcc \
    vim

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin::$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "api_service.py"]
