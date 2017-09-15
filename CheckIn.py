#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cookielib,urllib2
import urllib,json
class SMZDM(object):

    def __init__(self):

        self.baseUrl = "https://zhiyou.smzdm.com"
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    # 模拟登录
    def login(self):
        form = {"username": "账户名", "password": "密码"}

        postdata = urllib.urlencode(form)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',"Referer":"https://zhiyou.smzdm.com"}

        urllib2.install_opener(self.opener)

        req = urllib2.Request(self.baseUrl+"/user/login/ajax_check",data=postdata,headers=headers)

        req.add_header("Referer", "https://zhiyou.smzdm.com")

        resp = urllib2.urlopen(req)

        #for index, cookie in enumerate(self.cookies):
        #   print '[',index, ']',cookie;

        str = resp.read().encode("utf-8")

        print str

        a = json.loads(str)

        if a['error_code']==0:
            return True
        else:
            return False

    # 签到
    def checkin(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',"Referer":"https://zhiyou.smzdm.com"}

        urllib2.install_opener(self.opener)

        req = urllib2.Request(self.baseUrl+"/user/checkin/jsonp_checkin?callback=jQuery1124009342530301322993_1492518882274&_=1492518882276", headers=headers)

        resp = urllib2.urlopen(req)

        # for index, cookie in enumerate(self.cookies):
        #   print '[',index, ']',cookie;

        str = resp.read().encode("utf-8")

        print str


if __name__ == '__main__':
    smzdm = SMZDM()
    if smzdm.login():
        smzdm.checkin()