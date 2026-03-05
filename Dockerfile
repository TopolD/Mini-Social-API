FROM ubuntu:latest
LABEL authors="Topol"

ENTRYPOINT ["top", "-b"]