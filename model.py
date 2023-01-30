import pymysql
import base64
from db_classes import *
import os

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
            return False

class ProductModel:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='pythOn~2022', database='webproject')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def getProducts(self):
        product_list = []
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from products"
            self.__cursor.execute(query)
            data = self.__cursor.fetchall()
            for row in data:
                product_list.append({
                    'id': row[0],
                    'name': row[1],
                    'price': row[2],
                    'quantity': row[3],
                    'color': row[4],
                    'description' : row[7],
                    'image': row[8]
                })
                #product = Product(item[1],item[2],item[3],item[4],item[5],item[6],item[7],base64.b64encode(item[8]).decode('utf-8'))
                #product_list.append(product)
        except Exception as e:
            print(str(e))
        finally:
            return product_list

    def insertProduct(self,product):
        try:
            if self.__connection is None:
                self.connect()
            query = "insert into products(name,price,quantity,color,category,subcategory,description,image) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            args = (product.name,product.price,product.quantity,product.color,product.category,product.subcategory,product.description,product.image)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

