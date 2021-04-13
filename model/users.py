from config.config import DATABASE
import psycopg2
from flask_bcrypt import Bcrypt
from flask import jsonify

bcrypt = Bcrypt()

class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" %(DATABASE['dbname'], DATABASE['user'],
                                                                  DATABASE['password'], DATABASE['dbport'], DATABASE['host'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from \"Users\" where is_deleted = false;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from \"Users\" where uid = %s and is_deleted = false;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result
    
    def insertUser(self, first_name, last_name, username, password, email):
        cursor = self.conn.cursor()
        query = "insert into \"Users\" (first_name, last_name, username, password, email) values (%s,%s,%s,%s,%s) returning uid;"
        password = bcrypt.generate_password_hash(password).decode("utf-8")
        cursor.execute(query, (first_name, last_name, username, password, email))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def updateUser(self, uid, first_name, last_name, username, password, email):
        cursor = self.conn.cursor()
        query= "update \"Users\" set first_name=%s, last_name = %s, username=%s, password =%s, email=%s where uid=%s and is_deleted = false;"
        password = bcrypt.generate_password_hash(password).decode("utf-8")
        cursor.execute(query, (first_name, last_name, username, password, email, uid))
        self.conn.commit()
        return True

    def deleteUser(self, uid):
        cursor = self.conn.cursor()
        query = "update \"Users\" set is_deleted = true where uid=%s;"
        cursor.execute(query,(uid,))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows !=0
        