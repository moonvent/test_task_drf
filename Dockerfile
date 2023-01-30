FROM python:3.11
ENV PYTHONUNBUFFERED=1
RUN pip install "poetry==1.3.0"
WORKDIR /code
COPY . /code
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root
 
