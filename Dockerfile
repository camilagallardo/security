#FROM kalilinux/kali-rolling
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y install john hashcat
#RUN apt update && apt -y install kali-linux-headless
