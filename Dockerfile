FROM python:3.10.8-slim-buster

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Mr_Ghosts
WORKDIR /Mr_Ghosts
COPY . /Mr_Ghosts

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

CMD ["python", "bot.py"]
