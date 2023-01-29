FROM python:3.10.9-buster
WORKDIR /app
RUN chmod 777 /app
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python3", "botstatus_teletips.py"]
