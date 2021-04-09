from config.config import DATABASE
import psycopg2

class LikesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'], DATABASE['host'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getLikedById(self, l_mid):
        cursor = self.conn.cursor()
        query = "select lid, mid, uid from \"Likes\" where mid = %s and isLiked=true;"
        cursor.execute(query, (l_mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllLikesId(self, l_mid):
        cursor = self.conn.cursor()
        query = "select lid, mid, uid  from \"Likes\" where mid = %s and isLiked=true;"
        cursor.execute(query, (l_mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def likeMessage(self, l_mid, r_uid):
        cursor = self.conn.cursor()
        cursorCheck = self.conn.cursor()
        query = "Select lid from \"Likes\" where mid = %s and uid= %s;"
        queryCheck= "update \"Dislikes\" set isDisliked = false where (mid = %s and uid = %s);"
        cursor.execute(query, (l_mid, r_uid))
        lid = cursor.fetchone()
        if(lid):
            query1 = "update \"Likes\" set isLiked = true where lid = %s;"
            cursor.execute(query1, (lid,))
            cursorCheck.execute(queryCheck, (l_mid, r_uid))
        else:
            query2 = "Insert into \"Likes\" (mid, uid) values (%s,%s) returning lid;"
            cursor.execute(query2, (l_mid, r_uid))
            cursorCheck.execute(queryCheck, (l_mid, r_uid))

            lid = cursor.fetchone()[0]
        self.conn.commit()
        return lid

    def unlikeMessage(self, l_mid, r_uid):
        cursor = self.conn.cursor()
        query = "update \"Likes\" set isLiked = false where mid = %s and uid= %s returning lid;"
        cursor.execute(query, (l_mid, r_uid))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result