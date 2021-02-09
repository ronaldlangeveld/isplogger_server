FROM python:3.9-alpine

ADD script.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./script.py" ]
