
import urllib
import urllib2
import cookielib

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', ':Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]
urllib2.install_opener(opener)
req = urllib2.Request("https://zhiyou.smzdm.com/user/login/ajax_check", urllib.urlencode({"username": "用户名", "password": "密码"}))
req.add_header("Referer", "https://zhiyou.smzdm.com")

resp = urllib2.urlopen(req);

# for index, cookie in enumerate(cj):
#     print '[',index, ']',cookie;

str=resp.read().encode("utf-8")

print str


opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', ':Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]
urllib2.install_opener(opener)
req = urllib2.Request("http://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=jQuery1124009342530301322993_1492518882274&_=1492518882276")
req.add_header("Referer", "https://zhiyou.smzdm.com")

resp = urllib2.urlopen(req);

str=resp.read().encode("utf-8")
print str