# •6  cancelOrder(int userId, int orderId): check the userid and orderId already present in
# database and cancel the order. if any userId or orderId not present in database throw
# exception corresponding UserNotFound or OrderNotFound exception

class UserNotFoundException(Exception):
    def __init__(self, userId):
        self.user_id = userId
        super().__init__(f"User not found: {userId}")

