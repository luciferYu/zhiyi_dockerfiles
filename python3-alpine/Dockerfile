FROM alpine:3.8

MAINTAINER 81784779@qq.com

# 定义需要的DJANGO版本
ENV DJANGO_VER 2.1

# 拷贝安装pip的脚本
COPY get-pip.py /get-pip.py

# 设置alpine的镜像地址为阿里云的地址
RUN echo "https://mirrors.aliyun.com/alpine/v3.8/main/" > /etc/apk/repositories \
    # 更新安装 bash curl python3等工具
    && apk update \
    && apk add --no-cache bash \
    # 修改为从本地文件拷贝此脚本，不再需要curl工具
    #    curl \
    python3 \
    # 由于通过apk安装的pip总是基于python2.7的版本，不符合项目要求，此处使用get-pip.py的方式安装基于python3.6的pip
    # 下载get-pip.py脚本
    # 从本地文件拷贝，不再下载
    #    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    # 安装pip
    && python3 /get-pip.py \
    # 从阿里云的镜像安装特定版本的django
    && pip install django==$DJANGO_VER -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com \
    # 删除不必要的脚本
    && rm -f /get-pip.py \
    # 此环境专用做运行django项目，因此移除不必要的工具，减少空间
    && python3 -m pip uninstall -y pip setuptools wheel \
    #    && apk del curl \
    # 最后清空apk安装时产生的无用文件
    && rm -rf /var/cache/apk/*

# 暴露的端口
EXPOSE 50001

# 定义匿名卷，即为项目代码所在目录，挂载目录需要在run时指定
VOLUME /web

# 运行服务的命令
CMD ["python3", "/web/manage.py", "runserver", "0.0.0.0:50001"]
