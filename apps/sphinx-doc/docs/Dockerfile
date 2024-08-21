# --- BUILD ---
# Define a build argument for the version
ARG BASE_IMAGE_VERSION=0.1.1

# Use the build argument in the FROM instruction
FROM mpc-sphinx-doc-utils:${BASE_IMAGE_VERSION} as build

# Ensure the virtual environment is set up
ENV VIRTUAL_ENV="/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /usr/local/src/doc
COPY . .

RUN make html

# --- RUNTIME ---
FROM nginx:stable-alpine as runtime

WORKDIR /usr/share/nginx/html

WORKDIR /usr/share/nginx/html
COPY --from=build /usr/local/src/doc/build/html ./
