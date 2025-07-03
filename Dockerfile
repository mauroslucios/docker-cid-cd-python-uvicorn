FROM python:3.11-alpine3.20

WORKDIR /app



RUN apk update && apk upgrade && \
    apk add --no-cache gcc musl-dev linux-headers libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

#EXPOSE 8000
#CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port","8000", "--reload" ]


EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

