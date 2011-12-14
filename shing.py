#encoding:utf-8
#author:ty
#site:http://pythoner.net
#date:2011-10-28
"""
层叠发计算文章相似度
实例文本：用层叠发计算文本相似度有什么好处
设切片长度为5，则其切片如下：
用层叠发计->层叠发计算->叠发计算文->发计算文本...->有什么好处
"""
 
class ShingLing(object):
    """
    层叠法计算文本相似度
    """
    cut_step = 10  #切片字长
    text = []
    com_count = 0
     
    def __init__(self,text1,text2):
        self._cut(text1)
        self._cut(text2)
 
    def _cut(self,text):
        if len(text) < self.cut_step:
            return
         
        text = list(text)
        pice_list = []
        for i in range(len(text) - self.cut_step):
            pice = text[i:i + self.cut_step]
            pice_list.append(pice)
        re = {'pice':pice_list,'length':len(text)-self.cut_step}
        self.text.append(re)
 
    def com(self):
        pice1 = self.text[0]['pice']
        pice2 = self.text[1]['pice']
 
        for item in pice1:
            if item in pice2:
                self.com_count += 1
 
        total_length = self.text[0]['length'] + self.text[1]['length']
        com_count = self.com_count*2
        return com_count/float(total_length)
 
text1 = """请检查您的互联网连接状况，重新启动您可能正在使用的任何路由器、调制解调器以及其他网络设备。
检查您的 DNS 设置。如果您不确定是什么意思，请与您的网络管理员联系。
要尝试停用网络预测，请按以下步骤操作：转至扳手菜单 > 选项 > 高级选项，然后取消选中“预测网络操作，以提高网页载入速度”。如果该问题仍未得到解决，建议您重新选中此选项以提"""
text2 = """请检查您的互联网连接状况，重新启动您可能正在使用的任何路由器、调制解调器以及其他网络设备。
检查您的 DNS 设置。如果您不确定是什么意思，请与您的网络管理员联系"""
s = ShingLing(text1,text2)
 
print s.com()
