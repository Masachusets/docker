FROM python:3.10

COPY ./requirements.txt /api/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api

EXPOSE 8000

WORKDIR api

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]