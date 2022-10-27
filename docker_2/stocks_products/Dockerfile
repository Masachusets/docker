FROM python:3.10

COPY ./requirements.txt /stocks/requirements.txt
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r /stocks/requirements.txt

COPY . /stocks

EXPOSE 8000

WORKDIR stocks

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]