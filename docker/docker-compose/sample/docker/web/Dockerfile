FROM python:3.6-alpine
WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt	#sample的src在compose中volumes到src
CMD ["python3", "server.py"]