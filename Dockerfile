FROM python:3.10.8-slim-buster

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Micky_Streamer_Bot
WORKDIR /Micky_Streamer_Bot
COPY . /Micky_Streamer_Bot

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

CMD ["python", "bot.py"]
