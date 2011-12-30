#encoding:utf-8
import socket
import httplib
import time
import random
import threading

# web压力测试代码
# author:ty
# date:2011-12-30


socket.setdefaulttimeout(15)

class WebRequest(threading.Thread):
    threads_count = 100
    success_count = 0
    urls = []
    server_name = ''

    def __init__(self,server_name,urls):
        """
        初始化
        """
        threading.Thread.__init__(self)
        self.server_name = server_name
        self.urls = urls

    def request(self):
        """
        发起请求
        """
        self.curent_url = random.sample(self.urls,1)[0]
        connect = httplib.HTTPConnection(self.server_name)
        try:
            connect.request("GET",self.curent_url)
            response = connect.getresponse()
            response.read()
        except Exception,e:
            print '[thread %s] %s' %(self.getName(),e)
            return
        status = response.status
        print '[thread %s]%s-%s%s' %(self.getName(),status,self.server_name,self.curent_url)

        if status == 200:
            self.success_count += 1

    def run(self):
        while True:
            self.request()
            time.sleep(random.randrange(1,3))

s = ['/','/']
ths = []
for i in range(1000):
    #th = WebRequest('www.028jt.com',s)
    th = WebRequest('ddtcms.com',s)
    th.setName(i)
    ths.append(th)

for th in ths:
    th.start()








