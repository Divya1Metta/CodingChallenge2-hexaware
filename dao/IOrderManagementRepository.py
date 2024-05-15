# 6. Define an interface/abstract class named IOrderManagementRepository with methods for:
# • createOrder(User user, list of products): check the user as already present in database
# to create order or create user (store in database) and create order.
# • cancelOrder(int userId, int orderId): check the userid and orderId already present in
# database and cancel the order. if any userId or orderId not present in database throw
# exception corresponding UserNotFound or OrderNotFound exception
# • createProduct(User user, Product product): check the admin user as already present in
# database and create product and store in database.
# • createUser(User user): create user and store in database for further development.
# • getAllProducts(): return all product list from the database.
# • getOrderByUser(User user): return all product ordered by specific user from database.

from abc import ABC, abstractmethod
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from entity.user import User
from entity.product import Product

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user, products):
        pass

    @abstractmethod
    def cancelOrder(self, userId, orderId):
        pass

    @abstractmethod
    def createProduct(self, user, product):
        pass

    @abstractmethod
    def createUser(self, user):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, user):
        pass







