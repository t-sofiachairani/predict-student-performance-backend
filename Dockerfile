FROM python:3.15.0a3-alpine3.23

WORKDIR /app

COPY requirement.txt ./

RUN pip install -r requirement.txt

COPY . ./

CMD [ "flask","--app","src.app","run","--host=0.0.0.0", "--port=5000" ]