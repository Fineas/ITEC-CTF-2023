FROM python:3.10-slim-buster
RUN apt update -y && apt install -y xinetd && apt clean && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/crypto -u 8888 -m crypto
USER crypto

RUN pip3 install --no-cache-dir lark==1.1.5

COPY --chown=crypto:crypto xinetd /etc/xinetd.d/xinetd
COPY --chown=crypto:crypto chal /home/crypto
CMD ["/usr/sbin/xinetd", "-dontfork"]
