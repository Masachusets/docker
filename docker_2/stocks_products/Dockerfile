FROM python:3.10

WORKDIR stocks/

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /stocks/requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN chmod +x entrypoint.sh
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

#ENTRYPOINT ["stocks/entrypoint.sh"]