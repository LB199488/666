#Author:li bo
#!/usr/bin/python
# -*- coding: utf-8 -*-
from logging.handlers import HTTPHandler

import requests


import logging

#1.获取或创建xx记录器
logger = logging.getLogger("request")

#1.1设置记录器的日志等级（FATAL 50、ERROR 40、WARN 30、INFO 20、DEBUG  10、NOSET 0 ）
#等级高的，不会获取等级低的日志
logger.setLevel(logging.INFO)


#2.设置日志的格式
fmt_str ='[%(asctime)s%(levelname)s]%(message)s'
format = logging.Formatter(fmt = fmt_str,datefmt="%Y-%m-%d %H:%M:%S")

#3.设置日志处理器Handler
# - StreamHandler 控制台输出流
# - FileHandler  日志文件输出
# - HttpHandler  网络请求的日志上传处理器
handler = logging.StreamHandler()
file_handler = logging.FileHandler("test.log")
file_handler.setLevel((logging.WARN)#设置处理日志等级
http_handler = HTTPHandler(host = )


format=logging.Formatter('')