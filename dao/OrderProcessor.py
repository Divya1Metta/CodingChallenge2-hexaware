# 7. Implement the IOrderManagementRepository interface/abstractclass in a class called
# OrderProcessor. This class will be responsible for managing orders.



from dao.IOrderManagementRepository import IOrderManagementRepository
from entity.user import User
from entity.product import Product
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from util.DBConnUtil import getDBConn

class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.users = {}
        self.products = {}
        self.orders = {}

    def create_order(self, user: User, products: list):
        if user.user_id not in self.users:
            self.create_user(user)

        order_id = len(self.orders) + 1
        self.orders[(user.user_id, order_id)] = products

    def cancel_order(self, user_id: int, order_id: int):
        if (user_id, order_id) not in self.orders:
            raise OrderNotFoundException(f"Order {order_id} not found for user {user_id}")

        del self.orders[(user_id, order_id)]

    def create_product(self, user: User, product: Product):
        if user.user_id not in self.users or self.users[user.user_id].role != "Admin":
            raise UserNotFoundException("User not found or not an admin")

        product_id = len(self.products) + 1
        self.products[product_id] = product

    def create_user(self, user: User):
        if user.user_id in self.users:
            raise UserNotFoundException(f"User {user.user_id} already exists")

        self.users[user.user_id] = user

    def get_all_products(self):
        return self.products.values()

    def get_order_by_user(self, user: User):
        if user.user_id not in self.users:
            raise UserNotFoundException(f"User {user.user_id} not found")

        return self.orders.get((user.user_id,), [])
    




