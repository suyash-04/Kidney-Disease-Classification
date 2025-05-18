FROM python:3.11-slim-buster 
WORKDIR /app
COPY . /app

RUN apt update -y 
RUN apt-get update && pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]