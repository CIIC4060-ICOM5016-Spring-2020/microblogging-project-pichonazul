from config.config import DATABASE
import psycopg2



class MessagesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-52-45-73-150.compute-1.amazonaws.com'" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'])
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
        query = "select mid, uid, text, created_date, created_time from \"Messages\" where mid = %s;"
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
        query = "insert into \"Replies\" (uid, text, mid) values (%s,%s,%s) returning rid;"
        cursor.execute(query, (uid, text, mid))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
    
    def shareMessage(self, uid, mid):
        cursor = self.conn.cursor()        
        query = "insert into \"Shares\" (uid, mid) values (%s,%s) returning sid;"
        cursor.execute(query, (uid, mid))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid