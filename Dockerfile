FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || true

# Copy env file (optional)
COPY .env .env

# Install python-dotenv to load from .env if needed
RUN pip install python-dotenv

CMD ["python", "main.py"]
