FROM python:3.10.9

ARG PORT=8000

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-venv \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python3 -m venv $VIRTUAL_ENV

WORKDIR /app

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE $PORT

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]