FROM python:3.11.4

WORKDIR /

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gdal-bin \
  && rm -rf /var/lib/apt/lists/*

  COPY requirements.txt .

  RUN pip install --no-cache-dir -r requirements.txt

  COPY . .

  EXPOSE 8000

  CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
