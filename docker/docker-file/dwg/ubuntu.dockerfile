FROM debian:9.6

WORKDIR /data
COPY ODAFileConverter_QT5_lnxX64_4.7dll.deb .

RUN echo "deb http://mirrors.aliyun.com/debian stretch main contrib non-free\n\
  deb-src http://mirrors.aliyun.com/debian stretch main contrib non-free\n\
  deb http://mirrors.aliyun.com/debian stretch-updates main contrib non-free\n\
  deb-src http://mirrors.aliyun.com/debian stretch-updates main contrib non-free\n\
  deb http://mirrors.aliyun.com/debian-security stretch/updates main contrib non-free\n\
  deb-src http://mirrors.aliyun.com/debian-security stretch/updates main contrib non-free" >\
  /etc/apt/sources.list \
  && apt update \
  && apt install -y --no-install-recommends libqt5widgets5 \
  && dpkg -i ODAFileConverter_QT5_lnxX64_4.7dll.deb \
  && rm -rf /var/lib/apt/lists/* \
  && rm ODAFileConverter_QT5_lnxX64_4.7dll.deb

CMD ["/bin/bash"]