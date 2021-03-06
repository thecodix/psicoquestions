FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /psicoquestions
COPY requirements.txt /psicoquestions/requirements.txt
WORKDIR /psicoquestions

# Requirements installation
RUN pip install -r requirements.txt

CMD python run.py
