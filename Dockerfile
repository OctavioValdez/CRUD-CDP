FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ARG HOST
ARG USER
ARG PASSWORD
ARG NAME
ARG PORT

ENV HOST=$HOST
ENV USER=$USER
ENV PASSWORD=$PASSWORD
ENV NAME=$NAME
ENV PORT=$PORT

EXPOSE 5000 

CMD ["python", "crud.py"]