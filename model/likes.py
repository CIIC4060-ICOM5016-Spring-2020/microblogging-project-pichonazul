from config.config import DATABASE
import psycopg2

class LikesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-52-45-73-150.compute-1.amazonaws.com'" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getLikedById(self, l_mid):
        cursor = self.conn.cursor()
        query = "select lid, mid, uid from \"Likes\" where mid = %s and is_deleted=false;"
        cursor.execute(query, (l_mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllLikesId(self, l_mid):
        cursor = self.conn.cursor()
        query = "select lid, mid, uid  from \"Likes\" where uid = %s and is_deleted=false;"
        cursor.execute(query, (l_mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def likeMessage(self, r_uid, l_mid):
        cursor = self.conn.cursor()
        query = "Select * from \"Likes\" where mid = %s and uid= %s;"
        cursor.execute(query, (r_uid, l_mid))
        lid = cursor.fetchone()
        if(lid):
            query1 = "update \"Likes\" set is_deleted = false where lid = %s;"
            cursor.execute(query1, (lid))
        else:
            query2 = "Insert into \"Likes\" (mid, uid) values (%s,%s) returning lid;"
            cursor.execute(query2, (r_uid, l_mid))
            lid = cursor.fetchone()[0]
        self.conn.commit()
        return lid

    def unlikeMessage(self, r_uid, l_mid):
        cursor = self.conn.cursor()
        query = "update \"Likes\" set is_deleted=true where mid = %s and uid= %s returning lid;"
        cursor.execute(query, (r_uid, l_mid))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result