FROM python:3.10-slim

ARG SPOTIPY_CLIENT_ID
ARG SPOTIPY_CLIENT_SECRET
ARG SPOTIPY_REDIRECT_URI

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

ENV SPOTIPY_CLIENT_ID=$SPOTIPY_CLIENT_ID
ENV SPOTIPY_CLIENT_SECRET=$SPOTIPY_CLIENT_SECRET
ENV SPOTIPY_REDIRECT_URI=$SPOTIPY_REDIRECT_URI

ENTRYPOINT ["spotipy-utils"]
