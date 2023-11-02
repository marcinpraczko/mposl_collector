# BUILD: docker build -t mp/sphinx-doc:0.1.0 . 
# RUN  : docker run -it mp/sphinx-doc:0.1.0

# Looks like python docker are based on different distros
# INFO : https://hub.docker.com/_/python
# INFO : https://www.debian.org/releases/

FROM python:3.12-bullseye
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

# RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# SOLUTION: v01: Docker build with custom User and Group
ARG USER_ID
ARG GROUP_ID
ARG USER_LOGIN
RUN addgroup --gid $GROUP_ID $USER_LOGIN
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER_LOGIN

USER $USER_LOGIN

COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "bash" ]
