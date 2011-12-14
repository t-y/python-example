#encoding:utf-8
import MySQLdb

class Mysql(object):
    insert_id = 0
    sql = None

    def __init__(self,host,user,passwd,db='pythoner_db'):
        self.connect = MySQLdb.connect(host,user,passwd,db,charset="utf8")
        self.cursor = self.connect.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def execute(self,sql):
        self.sql = sql.encode('utf-8')
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception,e:
            print e,sql
            return False

        return True

    def query(self,sql):
        return self.execute(sql)

    def query_one(self, sql):
        sql = '%s LIMIT 1' %sql
        return self.execute(sql)

    def insert(self,sql):
        self.execute(sql)
        self.insert_id = self.connect.insert_id()
        return self.insert_id

    def close(self):
        slef.cursor.close()


if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    passwd = '123456'
    db = Mysql(host,user,passwd)
    sql1 = u"INSERT INTO wiki_entry (title,category_id,public,content,author_id,allow_comment,source,click_time) VALUES('测试啊',2,0,'test',1,1,'http://t-y.me',123)"
    print db.insert(sql1)
