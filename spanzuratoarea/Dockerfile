FROM python:3.10-slim-buster
RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/crypto2 -u 8888 -m crypto2
USER crypto2

RUN pip3 install --no-cache-dir lark==1.1.5

COPY --chown=crypto2:crypto2 xinetd /etc/xinetd.d/xinetd
COPY --chown=crypto2:crypto2 chal /home/crypto2

RUN chmod +x /home/crypto2/run.sh

CMD ["/usr/sbin/xinetd", "-dontfork"]
