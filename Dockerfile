FROM python:latest
COPY bot.py .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD ["bot.py"]