FROM lucifery/python3:v3.6


MAINTAINER 81784779@qq.com

RUN mkdir -p /data/web/WochuServerCenter/log/error /data/web/WochuServerCenter/log/request /data/web/WochuServerCenter/log/scripts

ADD WochuServerCenter /data/web/WochuServerCenter

ADD uwsgi.ini /data/web/WochuServerCenter/uwsgi.ini

RUN pip3 install -r /data/web/WochuServerCenter/requirements.txt

CMD ["/usr/local/python-3.6/bin/uwsgi","--ini","/data/web/WochuServerCenter/uwsgi.ini"]
