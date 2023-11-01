# BUILD: docker build -t mp/sphinx-doc:0.1.0 . 
# RUN  : docker run -it mp/sphinx-doc:0.1.0
# INFO : Release: Debian GNU/Linux / 11

FROM python:3.9.18

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "bash" ]
