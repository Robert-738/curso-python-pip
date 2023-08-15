FROM python:3.10

WORKDIR /app/images
COPY requeriments.txt /app/requeriments.txt
RUN pip install --no-cache-dir --upgrade -r /app/requeriments.txt
COPY . /app
WORKDIR /app

CMD bash -c "while true; do sleep 1; done"
