FROM python:3.9-slim-buster
LABEL maintainer="Arvind .A"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /chatapp
WORKDIR /chatapp

# install curl and nodejs
RUN apt-get update  && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    echo "nodejs version: $(node -v)" && \
    echo "npm version: $(npm -v)" && \
    npm run bootstrap && \
    npm run production && \
    npm cache clean --force

# Install python dependencies
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x /chatapp/scripts/entrypoint.sh && \
    mkdir -p /chatapp/staticfiles_build/static

# Uninstall nodejs and npm and remove cache
RUN apt-get purge -y nodejs && \
    apt-get purge -y curl && \
    apt-get autoremove -y && \
    apt-get autoclean -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.npm && \
    rm -rf /root/.cache && \
    rm -rf /chatapp/node_modules && \
    rm -rf /chatapp/.npm && \
    rm -rf /chatapp/apps/chatjs

CMD ["/chatapp/scripts/entrypoint.sh"]