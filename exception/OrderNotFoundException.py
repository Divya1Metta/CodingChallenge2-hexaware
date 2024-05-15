# 6• cancelOrder(int userId, int orderId): check the userid and orderId already present in
# database and cancel the order. if any userId or orderId not present in database throw
# exception corresponding UserNotFound or OrderNotFound exception
from exception import UserNotFoundException, OrderNotFoundException

def get_user(userId):
    if userId not in user:
        raise UserNotFoundException(userId)
    return user[userId]
try:
    user = get_user(userId)
    order = IOrderManagementRepository.get_order(orderId)   
except UserNotFoundException as e:
    print(f"User not found: {e}")
except OrderNotFoundException as e:
    print(f"Order not found: {e}")