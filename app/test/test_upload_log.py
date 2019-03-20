#Author:li bo
#!/usr/bin/python
# -*- coding: utf-8 -*-


from unittest import TestCase

import requests

from  requests import Request,Response


class TestLogger(TestCase):
    def test_query(self):
        url = 'http://localhost:5000/'
        resp:Response = requests.get(url)

        #断言响应的数据类型为200
        self.assertEquals(resp.status_code,200)

        #断言响应的数据类型为json
        self.assertEquals