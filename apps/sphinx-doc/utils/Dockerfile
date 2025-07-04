# Looks like python docker are based on different distros
# INFO : https://hub.docker.com/_/python
# INFO : https://www.debian.org/releases/

# FROM python:3.13.0a4-slim
FROM python:3.13.5-slim
LABEL maintainer="Marcin Praczko <marcin.praczko@gmail.com>"

WORKDIR /usr/local/src/app-build

# This dockerfile has been designed to work as a 'tool' container
# To compile some python modules `gcc` is required
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get -y install \
        gcc \
        graphviz \
        libgraphviz-dev \
        python3-pip \
        python3-venv \
        plantuml \
        rsync && \
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

# Sphinx-doc
COPY requirements/requirements-sphinx-doc.txt .
RUN pip install --no-cache-dir -r requirements-sphinx-doc.txt

# Tools
COPY requirements/requirements-tools.txt .
RUN pip install --no-cache-dir -r requirements-tools.txt

# Helpers scripts
COPY helpers ./helpers

# TODO: This image should work with the current user's UID and GID
# Switch to the 'appuser' user
# USER appuser

# CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "bash" ]
