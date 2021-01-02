FROM python:3.9

ADD script.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./script.py" ]

