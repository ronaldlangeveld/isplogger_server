FROM balenalib/raspberrypi3-python:latest

ADD script.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./script.py" ]
