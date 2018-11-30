FROM mdillon/postgis:11-alpine

ENV DISPLAY :0.0

RUN set -ex \
  && echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories \
  && apk update \
  && apk add --no-cache --virtual ca-certificates \
  && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
  && apk add --allow-untrusted glibc-2.28-r0.apk glibc-bin-2.28-r0.apk \
  && apk add --no-cache libx11 dpkg tar harfbuzz make g++ \
  && touch /var/lib/dpkg/status \
  && dpkg --add-architecture amd64 \
  && dpkg -i --force depends ODAFileConverter_QT5_lnxX64_4.7dll.deb \
  # && cd qt-everywhere-src-5.10.0 \
  # && ./configure -platform linux-g++ -mp -release -static -static-runtime -ltcg -prefix "/opt/Qt5.10.0/" -qt-sqlite \
  # -qt-pcre -plugin-sql-sqlite -plugin-sql-odbc -qt-zlib -qt-libpng -qt-libjpeg -opengl desktop -qt-freetype -no-qml-debug \
  # -no-angle -no-compile-examples -nomake tools -nomake tests -nomake examples -skip qtwebengine \
  # && make && make install
