FROM ubuntu:latest
LABEL authors="amir"

ENTRYPOINT ["top", "-b"]