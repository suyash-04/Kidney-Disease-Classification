FROM python:3.11-slim-buster 
WORKDIR /app
COPY . /app

EXPOSE 80
RUN apt update -y 
RUN apt-get update && pip install -r requirements.txt
CMD ["python", "app.py"]