FROM python:3.9.0

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./carford ./carford
COPY ./settings.toml ./settings.toml

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

# docker build -t viniciusvviterbo/advicehealth-api:latest .

# docker run --rm -p 5000:5000 --env-file ./.env --name advicehealth-api viniciusvviterbo/advicehealth-api:latest
