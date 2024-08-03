# BUILD: docker build -t mp/sphinx-doc:0.1.0 . 
# RUN  : docker run -it mp/sphinx-doc:0.1.0

# Looks like python docker are based on different distros
# INFO : https://hub.docker.com/_/python
# INFO : https://www.debian.org/releases/

FROM python:3.13.0rc1-slim

WORKDIR /usr/src/app

RUN pip install -U pip setuptools wheel

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "bash" ]
