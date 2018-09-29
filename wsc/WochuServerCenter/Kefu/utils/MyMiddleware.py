# -*- coding: utf-8 -*-
# Copyright 2018 WOCHU.CN All Rights Reserved                      #
# SYSTEM   : WochuServerCenter                                       
# FILENAME : @File : MyMiddleware.py                                       
# FUNCTION : 
# Author: YuZhiYi
# @Time : 2018/9/28 13:34
import time
import logging
from django.utils import deprecation
logger = logging.getLogger('django.request')


class AccessMiddleware(deprecation.MiddlewareMixin):
    def process_request(self,request):
        self.start_time = time.time()
        return None

    def process_response(self, request, response):
        use_time = time.time() - self.start_time
        req_meta = request.META
        logger.info("%s %s  %s %s %s %s %3.5f" % (req_meta['REQUEST_METHOD'],
        req_meta['PATH_INFO'], req_meta['REMOTE_ADDR'],
        req_meta['HTTP_USER_AGENT'],req_meta['SERVER_PROTOCOL'],response.status_code,use_time))
        return response
