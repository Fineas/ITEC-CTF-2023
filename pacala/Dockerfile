FROM ubuntu:20.04

# Invariants
ARG PORT=40000
ARG USERNAME=user
ENV USERNAME ${USERNAME}
RUN useradd -m $USERNAME
RUN apt-get update && apt-get install -y \
    python3 \
    xinetd \
    && rm -rf /var/lib/apt/lists/*

# Challenge files
ADD share /home/$USERNAME/
ADD xinetd.conf /etc/xinetd.d/chal
RUN chown root:root /home/$USERNAME
RUN chmod 444 /home/$USERNAME/*
RUN chmod +x /home/$USERNAME/run.sh /home/$USERNAME/pacala
EXPOSE $PORT

CMD [ \
        "xinetd", \
        "-dontfork", \
        "-f", "/etc/xinetd.d/chal" \
    ]
