FROM debian:bookworm

RUN apt-get update && apt-get install -y \
	nginx \
	tor \
	openssh-server && \
	mkdir -p /var/run/sshd && \
	rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf
COPY torrc /etc/tor/torrc
COPY sshd_config /etc/ssh/sshd_config
COPY /interface/index.html /var/www/html

RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

EXPOSE 80 4242

COPY exec.sh /usr/local/bin/exec.sh
RUN chmod +x /usr/local/bin/exec.sh
ENTRYPOINT ["/usr/local/bin/exec.sh"]
