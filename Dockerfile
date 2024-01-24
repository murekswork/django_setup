FROM python:3.10.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHOBUFFERED 1

WORKDIR /workdir

COPY ./requirements.txt .
RUN pip --default-timeout=20000 install -r requirements.txt

COPY . .