# 3. Create a subclass Electronics that inherits from Product. Add attributes specific to electronics
# products, such as:
# • brand (String)
# • warrantyPeriod (int)
from entity.product import Product
class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def warrantyPeriod(self):
        return self._warrantyPeriod

    @warrantyPeriod.setter
    def warrantyPeriod(self, value):
        self._warrantyPeriod = value