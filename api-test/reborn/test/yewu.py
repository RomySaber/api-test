#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
# class send_request(object):

host = 'http://192.168.10.197:8080'


class Test_platform(object):
    # 业务端接口
    def test_viewBusinessInfor(self):
        url = host + '/api/78dk/platform/business/viewBusinessInfor'
        try:
            data = json.dumps({"operateUser":"1","uid":"2"})
            header ={"Content-Type": "application/json"}
            response = requests.request('POST',url=url,data=data,headers=header)
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content.decode("utf-8")))
            return response.text
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == '__main__':
    Test_platform().test_viewBusinessInfor()
