FROM python:3

WORKDIR /opt/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./main.py" ]

EXPOSE 5000/tcp
