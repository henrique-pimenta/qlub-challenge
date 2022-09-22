FROM python:3.8

WORKDIR /src

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir --requirement ./requirements.txt

COPY ./ ./

EXPOSE 5000
