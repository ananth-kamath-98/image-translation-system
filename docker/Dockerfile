# docker/Dockerfile for Image Translation System Flask service
# Build from the project root with:
# docker build -f docker/Dockerfile -t image-translation-flask .

FROM python:3.9-slim

# set working directory inside container
WORKDIR /app

# copy requirements and install
COPY src/flask_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code
COPY ../src/flask_service/ .

# expose the port the app will run on
EXPOSE 5000

# start the app via gunicorn
# run.py defines 'app' variable as the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
