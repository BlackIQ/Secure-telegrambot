# Use Python
FROM python:latest

# Copy files
COPY app/bot.py .
COPY app/my_account.session .
COPY requirements.txt .

# Install requirments and Python stuff
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]

# Run bot
CMD ["bot.py"]