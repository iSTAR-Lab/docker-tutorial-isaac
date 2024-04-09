FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# COPY static/ static/
COPY templates/ templates/
COPY app.py .

VOLUME ["/uploads"]

EXPOSE 5050

ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050"]

#docker run -p 5050:5050 -e FLASK_SECRET_KEY=lsdkjffodsfj0wes --name picture_website image_view

#docker run -p 5050:5050 -e FLASK_SECRET_KEY=lsdkjffodsfj0wes -v pictures:/uploads --name picture_website image_view