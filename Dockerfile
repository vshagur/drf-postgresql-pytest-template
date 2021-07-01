FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install pip --upgrade \
    && pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:./"

COPY ./web /code/
