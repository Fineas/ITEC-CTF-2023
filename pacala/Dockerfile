FROM gcc:12.2.0-bullseye
RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/pwn -u 8888 -m pwn
USER pwn

COPY --chown=pwn:pwn xinetd /etc/xinetd.d/xinetd
COPY --chown=pwn:pwn chal /home/pwn

RUN chmod +x /home/pwn/*

CMD ["/usr/sbin/xinetd", "-dontfork"]