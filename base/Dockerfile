FROM centos:7

MAINTAINER 81784779@qq.com

#yum install
RUN yum install -y openssh-server rsync kde-l10n-Chinese libselinux-python openssl openssl-devel\
  && yum -y reinstall glibc-common \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/7/*

 #修改时区
RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#中文
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
ENV LC_ALL zh_CN.utf8

#limits.conf
ADD limits.conf /etc/security/limits.conf

#sshd 禁止密码登录
RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key  -N ''
RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
  && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \
  && sed -i "s/PasswordAuthentication.*/PasswordAuthentication no/g" /etc/ssh/sshd_config

#免密码登录
ADD authorized_keys /root/.ssh/authorized_keys