FROM python:3.9.5-alpine

LABEL maintainer="Nick Gonzales" \
      description="Sends catgirls at regular intervals to friends"

WORKDIR /app

RUN apk add tzdata && \
    cp /usr/share/zoneinfo/America/Chicago /etc/localtime && \
    echo "America/Chicago" > /etc/timezone && \
    apk del tzdata

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./scheduler.py ./scheduler.py
COPY ./catgirl.py ./catgirl.py

CMD ["python","./scheduler.py"]
