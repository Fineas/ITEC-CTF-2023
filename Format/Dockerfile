FROM python:3.10-slim-buster
RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/formeaza -u 8888 -m formeaza
USER formeaza

RUN pip3 install --no-cache-dir lark==1.1.5 

COPY --chown=formeaza:formeaza xinetd /etc/xinetd.d/xinetd
COPY --chown=formeaza:formeaza Chal /home/formeaza

RUN chmod +x /home/formeaza/*

CMD ["/usr/sbin/xinetd", "-dontfork"]
