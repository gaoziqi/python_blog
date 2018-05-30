FROM python:3.6-alpine	#alpine3.7版本
WORKDIR /src
ADD ../../src /src
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories && \ #添加国内镜像源
    apk update && \
    apk add --update --no-cache --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache postgresql-dev && \	#保留包
    pip3 install -r requirements.txt && \	#sample的src在compose中volumes到src
    apk del virtual-pkg-name  #清理virtual
CMD ["python3", "server.py"]