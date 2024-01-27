FROM tiangolo/uvicorn-gunicorn:python3.10 AS remuner-backend-base

RUN pip install --upgrade pip

COPY requirements/prod.txt /tmp/requirements/

RUN pip install -r /tmp/requirements/prod.txt

RUN mkdir /remuner-backend

WORKDIR /remuner-backend

COPY . ./

FROM remuner-backend-base AS remuner-backend-dev

COPY requirements/dev.txt /tmp/requirements/

RUN pip install -r /tmp/requirements/dev.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "debug"]

FROM remuner-backend-base AS remuner-backend-prod

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]