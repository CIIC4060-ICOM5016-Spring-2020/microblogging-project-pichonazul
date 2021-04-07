from config.config import DATABASE
import psycopg2

class BlocksDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-52-45-73-150.compute-1.amazonaws.com'" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getBlockedById(self, r_uid):
        cursor = self.conn.cursor()
        query = "select bid, registered_uid, blocked_uid from \"Blocks\" where registered_uid = %s and is_deleted=false;"
        cursor.execute(query, (r_uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUsersBlockingId(self, b_uid):
        cursor = self.conn.cursor()
        query = "select bid, registered_uid, blocked_uid from \"Blocks\" where blocked_uid = %s and is_deleted=false;"
        cursor.execute(query, (b_uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def blockUser(self, r_uid, b_uid):
        cursor = self.conn.cursor()
        query = "Select * from \"Blocks\" where registered_uid = %s and blocked_uid= %s;"
        cursor.execute(query, (r_uid, b_uid))
        bid = cursor.fetchone()
        if(bid):
            query1 = "update \"Blocks\" set is_deleted = false where bid = %s;"
            cursor.execute(query1, (bid))
        else:
            query2 = "Insert into \"Blocks\" (registered_uid, blocked_uid) values (%s,%s) returning bid;"
            cursor.execute(query2, (r_uid, b_uid))
            bid = cursor.fetchone()
        self.conn.commit()
        return bid

    def unblockUser(self, r_uid, b_uid):
        cursor = self.conn.cursor()
        query = "update \"Blocks\" set is_deleted=true where registered_uid = %s and blocked_uid= %s returning bid;"
        cursor.execute(query, (r_uid, b_uid))
        result = cursor.fetchone()
        self.conn.commit()
        return result