FROM python:3.10-slim-buster
RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/misc -u 8888 -m misc
USER misc

RUN pip3 install --no-cache-dir lark==1.1.5
RUN pip3 install requests

COPY --chown=misc:misc xinetd /etc/xinetd.d/xinetd
COPY --chown=misc:misc chal /home/misc

RUN chmod +x /home/misc/*

CMD ["/usr/sbin/xinetd", "-dontfork"]