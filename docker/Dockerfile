FROM python:3.10-slim

RUN pip install fastmcp

WORKDIR /app
COPY server.py /app/server.py

EXPOSE 8001

CMD ["python", "server.py"]
