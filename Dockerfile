From python:3.8
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /app
CMD  ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "15400"]