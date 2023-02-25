FROM python:3.8
#building a python docker so we mentioning which version python is

COPY requirements.txt requirements.txt
#source destination

RUN pip install -r requirements.txt

COPY ./src ./src
#copying from and to

CMD ["python", "./src/app.py" ]
#running python in src