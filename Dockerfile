FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update && apt-get install -y git
COPY requirements.txt /code/
RUN git config --global user.email "aberguecio1@uc.cl" \
    && git config --global user.name "aberguecio"
RUN pip install -r requirements.txt
COPY . /code/