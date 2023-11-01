# --- BUILD ---
FROM mpc-sphinx-doc-utils:0.1.0 as build

WORKDIR /usr/src/doc
COPY . .
RUN make html

# --- RUNTIME ---
FROM nginx:1.25.3
WORKDIR /usr/share/nginx/html

COPY --from=build /usr/src/doc/build/html ./

RUN find . -ls
