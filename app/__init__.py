#Author:li bo
#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import  Flask
from flask import Blueprint

app = False(__name__) #创建Flask应用服务

blue =Blueprint('blueprint',__name__)

app.register_buleprint(blue)