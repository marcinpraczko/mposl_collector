# BUILD: docker build -t mp/sphinx-doc:0.1.1 . 
# Run the Docker container with the current user's UID and GID
# RUN1  : docker run -it --user $(id -u):$(id -g) -v $(pwd):/usr/local/src/app-src-mounted mp/sphinx-doc:0.1.1
# RUN2  : docker run -it --user root:root -v $(pwd):/usr/local/src/app-src-mounted mp/sphinx-doc:0.1.1

# Looks like python docker are based on different distros
# INFO : https://hub.docker.com/_/python
# INFO : https://www.debian.org/releases/

# FROM python:3.13.0a4-slim
FROM python:3.12-slim
LABEL maintainer="Marcin Praczko <marcin.praczko@gmail.com>"

WORKDIR /usr/local/src/app-build

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
        python3-pip \
        python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define build arguments with default values
ARG USER_ID=1000
ARG GROUP_ID=1000

# ABU = App Build User
ENV ABU_USER_ID=${USER_ID}
ENV ABU_GROUP_ID=${GROUP_ID}
RUN addgroup --gid $ABU_GROUP_ID appuser
RUN useradd --create-home --shell /bin/bash --uid $ABU_USER_ID --gid $ABU_GROUP_ID --comment 'App Build User' appuser
RUN chown -R appuser:appuser /usr/local/src/app-build

# https://realpython.com/python-versions-docker/
ENV VIRTUAL_ENV="/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -U pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the 'appuser' user
# USER appuser

# CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "bash" ]
