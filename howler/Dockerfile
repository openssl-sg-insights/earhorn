FROM jrottenberg/ffmpeg:4-alpine

RUN apk add --update --no-cache python3 icecast tini
ADD howler.py howler.py

EXPOSE 8000

ENTRYPOINT ["/sbin/tini", "--", "./howler.py"]
