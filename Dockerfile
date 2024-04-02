FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

#COPY static/ static/
COPY templates/ templates/
COPY app.py .

VOLUME ["/uploads"]

EXPOSE 5000

ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]