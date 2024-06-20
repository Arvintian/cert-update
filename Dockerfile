FROM registry.cn-beijing.aliyuncs.com/liteyun-labs/python:3.10.14-alpine3.20

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -U pip && pip install -r /app/requirements.txt
ADD . /app/

ENTRYPOINT ["python","/app/main.py"]