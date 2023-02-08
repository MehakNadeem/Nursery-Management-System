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

    def getUserID(self,email):
        id_ = None
        try:
            if self.__connection is None:
                self.connect()
            query = "select ID from user where email = %s"
            args = (email)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchone()
            id_ = data[0]
        except Exception as e:
            print(str(e))
        finally:
            return id_

    def getUserByID(self,usrID):
        user = None
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from user where ID = %s"
            args = (usrID)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchone()
            user = User(data[1],data[2],data[3])
        except Exception as e:
            print(str(e))
        finally:
            return user

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

    def updateName(self, name, email):
        try:
            if self.__connection is None:
                self.connect()
            userID = self.getUserID(email)
            query = "UPDATE user SET name = %s WHERE ID = %s"
            args = (name,userID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def updateEmail(self, newEmail, email):
        try:
            if self.__connection is None:
                self.connect()
            userID = self.getUserID(email)
            query = "UPDATE user SET email = %s WHERE ID = %s"
            args = (newEmail,userID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def updatePassword(self, newpsw, email):
        try:
            if self.__connection is None:
                self.connect()
            userID = self.getUserID(email)
            query = "UPDATE user SET password = %s WHERE ID = %s"
            args = (newpsw,userID)
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
                    'quantity': row[2],
                    'price': row[3],
                    'color': row[4],
                    'description' : row[7],
                    'image': row[8]
                })
        except Exception as e:
            print(str(e))
        finally:
            return product_list

    def getProductByID(self,prodID):
        product_ = None
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from products where p_id = %s"
            args = (prodID)
            self.__cursor.execute(query,args)
            row = self.__cursor.fetchone()
            product_ = Product(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            if product_ is not None:
                if product_.quantity == '0':
                    product_ = None
        except Exception as e:
            print(str(e))
        finally:
            return product_

    def updateQuantityByPid(self, prod_id, quantity):
        try:
            if self.__connection is None:
                self.connect()
            query = "UPDATE products SET quantity = %s WHERE ( p_id = %s )"
            args = (quantity,prod_id)
            self.__cursor.execute(query, args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False


    def insertProduct(self,product):
        try:
            if self.__connection is None:
                self.connect()
            query = "insert into products(name,quantity,price,color,category,subcategory,description,image) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            args = (product.name,product.quantity,product.price,product.color,product.category,product.subcategory,product.description,product.image)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def getFertilizer(self, category, subcategory):
        product_list = []
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from products where category = %s and subcategory = %s"
            args = (category,subcategory)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchall()
            for row in data:
                product_list.append({
                    'id': row[0],
                    'name': row[1],
                    'quantity': row[2],
                    'price': row[3],
                    'color': row[4],
                    'category' : row[5],
                    'subcategory' : row[6],
                    'description': row[7],
                    'image': row[8]
                })
        except Exception as e:
            print(str(e))
        finally:
            return product_list



class OrdersModel:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='pythOn~2022', database='webproject')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def getOrders(self):
        order_list = []
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from `order`"
            self.__cursor.execute(query)
            data = self.__cursor.fetchall()
            for item in data:
                order = Order(item[1],item[2],item[3])
                order_list.append(order)
        except Exception as e:
            print(str(e))
        finally:
            return order_list

    def getOrdersByCustomerID(self, custID):
        order_list = []
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from `order` where customer_id = %s"
            args = (custID)
            self.__cursor.execute(query, args)
            data = self.__cursor.fetchall()
            for item in data:
                order_list.append(
                    {'id' : item[0],
                     'date' : item[1],
                     'status' : item[2],
                     'amount' : item[3]}
                )
        except Exception as e:
            print(str(e))
        finally:
            return order_list


class CustomerModel:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='pythOn~2022', database='webproject')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def getCustomerByUserID(self,usrID):
        customer = None
        try:
            if self.__connection is None:
                self.connect()
            query = "select * from customer where user_id = %s"
            args = (usrID)
            self.__cursor.execute(query,args)
            data = self.__cursor.fetchone()
            db = UserModel()
            user_data = db.getUserByID(usrID)
            cust_id = data[0]
            customer = Customer(user_data.name,user_data.email,user_data.password,data[1],data[2],data[3],data[4],data[5],data[7])
        except Exception as e:
            print(str(e))
        finally:
            return cust_id,customer

    def updatePhoneNo(self, phoneno, email):
        try:
            if self.__connection is None:
                self.connect()
            db_user = UserModel()
            userID = db_user.getUserID(email)
            query = "UPDATE customer SET phone = %s WHERE user_id = %s"
            args = (phoneno,userID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def updateAddress(self, address, email):
        try:
            if self.__connection is None:
                self.connect()
            db_user = UserModel()
            userID = db_user.getUserID(email)
            query = "UPDATE customer SET address = %s WHERE user_id = %s"
            args = (address,userID)
            self.__cursor.execute(query,args)
            self.__connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False



