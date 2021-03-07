# We're using Ubuntu 20.10
FROM irhamfadzillah/yama:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b x-sql-extended https://github.com/ichn666shit/Yama /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ichn666shit/Yama/x-sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
