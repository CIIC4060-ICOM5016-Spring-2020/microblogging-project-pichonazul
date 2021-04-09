from config.config import DATABASE
import psycopg2

class DislikesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'], DATABASE['host'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getDislikedById(self, d_mid):
        cursor = self.conn.cursor()
        query = "select did, mid, uid from \"Dislikes\" where mid = %s and isDisliked=true;"
        cursor.execute(query, (d_mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllDislikesId(self, d_mid):
        cursor = self.conn.cursor()
        query = "select did, mid, uid  from \"Dislikes\" where mid = %s and isDisliked=true;"
        cursor.execute(query, (d_mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def dislikeMessage(self, d_mid, r_uid):
        cursor = self.conn.cursor()
        cursorCheck = self.conn.cursor()

        query = "Select did from \"Dislikes\" where mid = %s and uid= %s;"
        queryCheck= "update \"Likes\" set isLiked = false where (mid = %s and uid = %s);"
        cursor.execute(query, (d_mid, r_uid))
        did = cursor.fetchone()
        if(did):
            query1 = "update \"Dislikes\" set isDisliked = true where did = %s;"
            cursor.execute(query1, (did,))
            cursorCheck.execute(queryCheck, (d_mid, r_uid))
        else:
            query2 = "Insert into \"Dislikes\" (mid, uid) values (%s,%s) returning did;"
            cursor.execute(query2, (d_mid, r_uid))
            cursorCheck.execute(queryCheck, (d_mid, r_uid))
            did = cursor.fetchone()[0]
        self.conn.commit()
        return did

    def undislikeMessage(self, d_mid, r_uid):
        cursor = self.conn.cursor()
        query = "update \"Dislikes\" set isDisliked = false where mid = %s and uid= %s returning did;"
        cursor.execute(query, (d_mid, r_uid))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result