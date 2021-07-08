FROM docker.io/library/python:slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_CONFIG=development
ENV FLASK_APP=run.py
CMD ["flask","run"]