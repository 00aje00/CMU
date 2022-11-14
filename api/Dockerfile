# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python3", "main.py", "--host=0.0.0.0" ]
#ENTRYPOINT [ "python" ]
#CMD [ "main.py" ]
