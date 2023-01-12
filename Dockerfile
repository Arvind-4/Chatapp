FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - &&\
    apt-get install -y nodejs   

COPY . /chatapp
WORKDIR /chatapp

RUN python3 -m venv /opt/venv && \
   /opt/venv/bin/pip install pip --upgrade && \
   /opt/venv/bin/pip install -r requirements.txt && \
   npm run i && \
   npm run production && \
   mkdir -p /chatapp/staticfiles_build/static && \
   chmod +x /chatapp/scripts/entrypoint.sh && \
   chmod +x /chatapp/scripts/release.sh && \
   sh /chatapp/scripts/release.sh

EXPOSE 8000/tcp
CMD ["sh", "/chatapp/scripts/entrypoint.sh"]