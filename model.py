import pymysql
from db_classes import *

class UserModel:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='pythOn~2022', database='webproject')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def getUsers(self):
        user_list = []
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from user"
            self.__cursor.execute(query)
            data = self.__cursor.fetchall()
            for item in data:
                user = User(item[1], item[2], item[3])
                user_list.append(user)
        except Exception as e:
            print(str(e))
        finally:
            return user_list

    def insertUser(self,user):
        try:
            if self.__connection is None:
                self.connect()
            query = "insert into user(name,email,password) values (%s,%s,%s)"
            args = (user.name,user.email,user.password)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
