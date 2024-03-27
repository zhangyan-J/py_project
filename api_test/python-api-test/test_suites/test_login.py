#!/usr/bin/python
# coding=utf-8
from apis.pithy_api import PithyAPP


class TestApi(object):

    def test_get(self):
        """
        测试get方法
        """

        app = PithyAPP()
        res = app.get().json
        assert res.args.key1 == u'value1'