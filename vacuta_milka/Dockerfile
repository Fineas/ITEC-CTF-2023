FROM python:3.8-slim-buster

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install cowsay -y
RUN pip3 install -r requirements.txt

RUN groupadd -r swuser -g 433 && \
    useradd -u 431 -r -g swuser -s /sbin/nologin -c "Docker image user" swuser

COPY . .

USER swuser

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
