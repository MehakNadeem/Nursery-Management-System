class User:
    """user class"""
    def __init__(self,name='',email='',password=''):
        self.name=name
        self.email=email
        self.password=password

class Customer(User):
    """customer class"""
    def __init__(self,name='',email='',password='',phone = '', address = '',
                 city = '', province = '', zipCode = '', orderCount = 1):
        User.__init__(name,email,password)
        self.phone = phone
        self.address = address
        self.city = city
        self.province = province
        self.zipCode = zipCode
        self.orderCount = orderCount

class Product:
    """product class"""
    def __init__(self,name = '',price = 0.00,quantity = 1,color = '',category = '',
                 subcategory = '',description = '',image = ''):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color
        self.category = category
        self.subcategory = subcategory
        self.description = description
        self.image = image

    def print(self):
        print(self.name,self.price,self.quantity,self.color,self.category,self.subcategory,self.description,self.image)

class Order:
    """order class"""
    def __init__(self,date='',status='',amount=0.00):
        self.date = date
        self.status = status
        self.amount = amount
