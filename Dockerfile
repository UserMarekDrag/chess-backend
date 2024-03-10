FROM python:3.10

RUN apt-get update && apt-get install -y graphviz libgraphviz-dev

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
