FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install --proxy http://jpnproxy.jp.ibm.com:8080/ --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]

ENV http_proxy http://jpnproxy.jp.ibm.com:8080/
ENV https_proxy http://jpnproxy.jp.ibm.com:8080/
