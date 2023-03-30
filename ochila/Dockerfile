FROM gcc:12.2.0-bullseye

RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/formeaza -u 8888 -m formeaza
USER formeaza 

COPY --chown=formeaza:formeaza xinetd /etc/xinetd.d/xinetd
COPY --chown=formeaza:formeaza Chal /home/formeaza

RUN chmod +x /home/formeaza/*

CMD ["/usr/sbin/xinetd", "-dontfork"]
