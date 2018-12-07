FROM lucifery/python3-alpine:v3.6.6

MAINTAINER 81784779@qq.com

ENV PROJECT pythontools
# 拷贝安装pip的脚本
COPY get-pip.py /get-pip.py
COPY requirements.txt /web/requirements.txt


RUN apk add --no-cache gcc build-base python3-dev uwsgi-python3 \
    && python3 /get-pip.py \
    && python3 -m pip install -r  /web/requirements.txt \
    && rm -rf /var/cache/apk/*




# 暴露的端口
EXPOSE 50001

# 定义匿名卷，即为项目代码所在目录，挂载目录需要在run时指定
VOLUME /web

# 运行服务的命令
# uwsgi --chdir /web  --plugin python3 --wsgi-file  ./WochuServerCenter/wsgi.py --static-map /static=/web/static --pidfile=/var/run/wsc.pid --http-socket 0.0.0.0:8000
WORKDIR /web
#CMD ["uwsgi", "--chdir","/web","--plugin","python3","--wsgi-file","./WochuServerCenter/wsgi.py","--static-map","/static=/web/static","--pidfile=/var/run/WochuServerCenter.pid","--master","--processes=2","--threads=4","--http-socket","0.0.0.0:50001"]
ENTRYPOINT uwsgi  --plugin python3 --wsgi-file  ./${PROJECT}/wsgi.py --pidfile=/var/run/${PROJECT}.pid --master --processes=2 --threads=4 --http-socket 0.0.0.0:50001
