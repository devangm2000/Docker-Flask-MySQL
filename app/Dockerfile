FROM python:3.7
COPY . /app
WORKDIR /app
#ENV FLASK_APP flask_api.py
#ENV FLASK_RUN_HOST 0.0.0.0
#COPY requirements.txt /app
RUN pip install -r requirements.txt 
#EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["flask_api.py"]

#-h 127.0.0.1 -p 5000


