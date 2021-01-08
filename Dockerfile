FROM python:3.7.7-slim
RUN pip install pipenv

WORKDIR /api/

COPY ./api/ /api/
COPY Pipfile /api/Pipfile

RUN pipenv install --skip-lock

CMD ["pipenv", "run", "gunicorn", "-c", "gunicorn.ini", "app:APP"]
