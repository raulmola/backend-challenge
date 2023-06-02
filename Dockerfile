FROM python:3.9 AS botassistanceapi

COPY app /app 

RUN pip install -r app/requirements.txt

ENTRYPOINT ["python", "/app/main.py"]


