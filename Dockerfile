FROM python:3.10-slim

RUN useradd --create-home --shell /bin/bash spotipy

WORKDIR /home/spotipy

COPY requirements.txt ./
COPY setup.py ./
RUN pip install --no-cache-dir -r requirements.txt

USER spotipy
COPY . .

USER root
RUN pip install --editable .

USER spotipy

ENTRYPOINT ["spotipy-utils"]
