FROM python:3.9.20-alpine3.20

WORKDIR /app

# Install dependencies for psyhog2
RUN apk add --no-cache postgresql-dev

RUN pip install pipenv

COPY Pipfile* .

RUN pipenv install 

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000"]
