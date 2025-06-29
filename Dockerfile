FROM python:3.12-slim

WORKDIR P:\\temp\\船赛\\backend

COPY requirements.txt .
COPY app.py .
COPY JoyStick.py .
COPY Camera.py .
COPY Serial.py .

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "app.py"]
