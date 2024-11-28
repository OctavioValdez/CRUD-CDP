FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ARG HOST
ARG USER
ARG PASSWORD
ARG NAME

ENV HOST=$HOST
ENV USER=$USER
ENV PASSWORD=$PASSWORD
ENV NAME=$NAME

EXPOSE 5000 

CMD ["python", "app.py"]