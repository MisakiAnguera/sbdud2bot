FROM python:3.9-slim
COPY files/ /files/
COPY apis.py basededatos.py bot.py csv_json.py requirements.txt scraping.py /
RUN pip install -r requirements.txt
CMD ["python","./bot.py"]