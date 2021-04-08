from config.config import DATABASE
import psycopg2

class FollowsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-52-45-73-150.compute-1.amazonaws.com'" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getFollowedById(self, r_uid):
        cursor = self.conn.cursor()
        query = "select fid, uid, followed_user from \"Follows\" where uid = %s and is_deleted=false;"
        cursor.execute(query, (r_uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUsersFollowingId(self, f_uid):
        cursor = self.conn.cursor()
        query = "select fid, uid, followed_user from \"Follows\" where followed_user = %s and is_deleted=false;"
        cursor.execute(query, (f_uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def followUser(self, r_uid, f_uid):
        cursor = self.conn.cursor()
        query = "Select fid from \"Follows\" where uid = %s and followed_user= %s;"
        cursor.execute(query, (r_uid, f_uid))
        fid = cursor.fetchone()[0]
        if(fid):
            query1 = "update \"Follows\" set is_deleted = false where fid = %s;"
            cursor.execute(query1, (fid,))
        else:
            query2 = "Insert into \"Follows\" (uid, followed_user) values (%s,%s) returning fid;"
            cursor.execute(query2, (r_uid, f_uid))
            fid = cursor.fetchone()[0]
        self.conn.commit()
        return fid

    def unfollowUser(self, r_uid, f_uid):
        cursor = self.conn.cursor()
        query = "update \"Follows\" set is_deleted=true where uid = %s and followed_user= %s returning fid;"
        cursor.execute(query, (r_uid, f_uid))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result