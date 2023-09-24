FROM python:3-alpine

WORKDIR /app

COPY src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY src /app

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "--reload"]