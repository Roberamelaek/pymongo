FROM python
WORKDIR /app
COPY messages.py /app
RUN pip install termcolor pymongo
CMD [ "python3","messages.py" ]