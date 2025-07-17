FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY scripts/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

CMD ["/bin/bash", "-c", "/wait-for-it.sh noxer_db:5432 -t 60 && sleep 5 && python -m api_server.main"]

