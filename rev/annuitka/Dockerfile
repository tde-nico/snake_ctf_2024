FROM python:3.12.5-bullseye

RUN pip3 install --no-cache-dir cryptography
COPY chall /chall
COPY linux_server /ida

EXPOSE 23946

ENTRYPOINT ["/chall"]