FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY .env ./

COPY requirements.txt ./

RUN apk add --no-cache gcc libc-dev mariadb-connector-c-dev 
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD [ "python", "./app.py" ]
