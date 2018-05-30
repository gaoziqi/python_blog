# alpine3.7版本
FROM python:3.6-alpine
ADD . /src
WORKDIR /src


# 添加国内镜像源: echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories
# 保留包: apk add --no-cache postgresql-dev
# 清理virtual: apk del virtual-pkg-name
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories && \
    apk update && \
    apk add --update --no-cache --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache postgresql-dev && \
    pip3 install -r requirements.txt && \
    apk del virtual-pkg-name

CMD ["python3", "server.py"]