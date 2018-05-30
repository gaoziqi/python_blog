FROM python:3.6
WORKDIR /src
RUN /bin/bash -c ls /src
RUN pip install -r requirements.txt	#sample的src在compose中volumes到src
CMD ["python3", "server.py"]