FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD script.py .

CMD [ "python", "./script.py" ]
