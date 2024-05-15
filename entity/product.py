# 1. Create a base class called Product with the following attributes:
# • productId (int)
# • productName (String)
# • description (String)
# • price (double)
# • quantityInStock (int)
# • type (String) [Electronics/Clothing]
# 2. Implement constructors, getters, and setters for the Product class.
class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    @property
    def productId(self):
        return self._productId

    @productId.setter
    def productId(self, value):
        self._productId = value

    @property
    def productName(self):
        return self._productName

    @productName.setter
    def productName(self, value):
        self._productName = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantityInStock(self):
        return self._quantityInStock

    @quantityInStock.setter
    def quantityInStock(self, value):
        self._quantityInStock = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value