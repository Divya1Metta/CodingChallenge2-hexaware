import pyodbc
from entity.user import User
from entity.product import Product
from entity.electronics import Electronics
from entity.clothing import Clothing
from dao.OrderProcessor import OrderProcessor
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
server_name = "LAPTOP-K22HCAQN\SQLEXPRESS"
database_name = "CodingChallenge2DB"
 

conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Select 1")
print("Database connection is successful 🎊")
 

# OrderManagement.py
class OrderManagement:
    """
    Main class to simulate the order management system.
    """
    def __init__(self):
        self.order_processor = OrderProcessor()

    def main(self):
        """
        Main method to simulate the order management system.
        """
        while True:
            print("Order Management System")
            print("1. Create User")
            print("2. Create Product")
            print("3. Cancel Order")
            print("4. Get All Products")
            print("5. Get Order by User")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.create_product()
            elif choice == "3":
                self.cancel_order()
            elif choice == "4":
                self.get_all_products()
            elif choice == "5":
                self.get_order_by_user()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_user(self):
        """
        Creates a new user.
        """
        user_id = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")
        user = User(user_id, username, password, role)
        self.order_processor.create_user(user)
        print("User created successfully!")

    def create_product(self):
        """
        Creates a new product.
        """
        product_id = int(input("Enter product ID: "))
        product_name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantity_in_stock = int(input("Enter quantity in stock: "))
        type = input("Enter product type (Electronics/Clothing): ")
        if type == "Electronics":
            brand = input("Enter brand: ")
            warranty_period = int(input("Enter warranty period: "))
            product = Electronics(product_id, product_name, description, price, quantity_in_stock, type, brand, warranty_period)
        elif type == "Clothing":
            size = input("Enter size: ")
            color = input("Enter color: ")
            product = Clothing(product_id, product_name, description, price, quantity_in_stock, type, size, color)
        else:
            print("Invalid product type. Please try again.")
            return
        self.order_processor.create_product(product)
        print("Product created successfully!")

    def cancel_order(self):
        """
        Cancels an order.
        """
        user_id = int(input("Enter user ID: "))
        order_id = int(input("Enter order ID: "))
        try:
            self.order_processor.cancel_order(user_id, order_id)
            print("Order cancelled successfully!")
        except UserNotFoundException:
            print("User not found!")
        except OrderNotFoundException:
            print("Order not found!")

    def get_all_products(self):
        """
        Retrieves all products.
        """
        products = self.order_processor.get_all_products()
        for product in products:
            print(product)

    def get_order_by_user(self):
        """
        Retrieves orders by user.
        """
        user_id = int(input("Enter user ID: "))
        orders = self.order_processor.get_order_by_user(user_id)
        for order in orders:
            print(order)

if __name__ == "__main__":
    order_management = OrderManagement()
    order_management.main()
choice=int(input("please enter a choice:"))

conn.close()



