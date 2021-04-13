from config.config import DATABASE
import psycopg2



class MessagesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'], DATABASE['host'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select mid, uid, text, created_date, created_time from \"Messages\" where isdeleted = false;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, uid, text, created_date, created_time from \"Messages\" where mid = %s and isdeleted = false;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result
    
    def postMessage(self, uid, text):
        cursor = self.conn.cursor()
        query = "insert into \"Messages\" (uid, text) values (%s,%s) returning mid;"
        cursor.execute(query, (uid, text))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid
    
    def replyMessage(self, uid, text, mid):
        cursor = self.conn.cursor()
        muid = "select uid from \"Messages\" where mid = %s;"
        cursor.execute(muid, (mid,))
        muid = cursor.fetchone()[0]
        query2 = "select blocked_uid from \"Blocks\" where (is_deleted = false and blocked_uid = %s and registered_uid = %s);"
        cursor.execute(query2, (uid, muid))
        query2 = cursor.fetchone()
        if(query2 == None):
            query3 = "insert into \"Replies\" (uid, text, mid) values (%s,%s,%s) returning rid;"
            cursor.execute(query3, (uid, text, mid))
            rid = cursor.fetchone()[0]
        else:
            rid = 0
        self.conn.commit()
        return rid
       
    
    def shareMessage(self, uid, mid):
        cursor = self.conn.cursor()
        muid = "select uid from \"Messages\" where mid = %s;"
        cursor.execute(muid, (mid,))
        muid = cursor.fetchone()[0]
        query2 = "select blocked_uid from \"Blocks\" where (is_deleted = false and blocked_uid = %s and registered_uid = %s);"
        cursor.execute(query2, (uid, muid))
        query2 = cursor.fetchone()
        if(query2 == None):
            query3 = "insert into \"Shares\" (uid, mid) values (%s,%s) returning sid;"
            cursor.execute(query3, (uid, mid))
            sid = cursor.fetchone()[0]
        else:
            sid = 0
        self.conn.commit()
        return sid
        