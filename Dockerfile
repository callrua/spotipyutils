# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
WORKDIR /app/webserver
ENV SPOTIPY_CLIENT_ID="82365394a6aa4f3899e9894543c5e45d"
ENV SPOTIPY_CLIENT_SECRET="825a853dbdd748f8b0a46861b98452e5"
ENV SPOTIPY_REDIRECT_URI="http://localhost/"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]