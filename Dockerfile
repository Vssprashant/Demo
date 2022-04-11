FROM ubuntu
MAINTAINER prashant vss <vss.prashant302@gmail.com>

RUN apt-get update

CMD["echo", "My first docker image"]
