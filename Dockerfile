FROM python:latest
COPY bot.py .
COPY my_account.session .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["bot.py"]