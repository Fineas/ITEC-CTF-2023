FROM python:3.10-slim-buster
RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/crypto3 -u 8888 -m crypto3
USER crypto3

RUN pip3 install --no-cache-dir lark==1.1.5
RUN pip3 install requests

COPY --chown=crypto3:crypto3 xinetd /etc/xinetd.d/xinetd
COPY --chown=crypto3:crypto3 chal /home/crypto3

RUN chmod +x /home/crypto3/*

CMD ["/usr/sbin/xinetd", "-dontfork"]
