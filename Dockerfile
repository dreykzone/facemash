FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /app/instance

EXPOSE 5000

CMD ["sh", "-c", "flask --app run.py db upgrade && flask --app run.py seed && gunicorn --bind 0.0.0.0:5000 run:app"]