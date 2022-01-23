FROM ubuntu:20.04
WORKDIR /tool
COPY . /tool
RUN apt-get update
RUN apt-get install -y git && apt-get install -y python3 && apt-get install -y python3-pip
RUN chmod +x /tool/setup.sh
RUN mkdir /root/Desktop
