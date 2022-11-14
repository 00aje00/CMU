# syntax=docker/dockerfile:1
FROM python:3.8

# definding a working directory to copy api code into 
WORKDIR /app
COPY . .

# installing the api dependencies and requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python3", "main.py", "--host=0.0.0.0" ]
