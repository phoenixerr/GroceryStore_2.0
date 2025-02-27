from application.models import *
from application.cache import cache

@cache.memoize()
def get_all_categories():
    categories = Category.query.all()
    return [category.to_dict() for category in categories]
    

@cache.memoize()
def get_all_products():
    products = Product.query.all()
    return products

@cache.memoize()
def get_booking_by_id(bookingid):
    booking = Booking.query.filter_by(bookingid=bookingid).first()
    return booking.to_dict()

@cache.memoize()
def get_order_by_id(orderid):
    order = Order.query.filter_by(orderid=orderid).first()
    return order.to_dict()


@cache.memoize()
def get_user_bookings(user_id):
    bookings = Booking.query.filter_by(user_id=user_id)
    return [booking.to_dict() for booking in bookings]

@cache.memoize()
def get_user_orders(user_id):
    orders = Order.query.filter_by(userid=user_id).all()
    return [order.to_dict() for order in orders]

@cache.memoize()
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    return user

@cache.memoize()
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

@cache.memoize()
def get_token_by_user_id(user_id):
    token = Token.query.filter_by(user_id=user_id).first().token
    return token

@cache.memoize()
def get_user_id_by_token(token):
    user_id = Token.query.filter_by(token=token).first().user_id
    return user_id

@cache.memoize()
def get_status(user_id):
    visited=Visited.query.filter_by(user_id=user_id).first()
    return visited

@cache.memoize()
def get_user_approval(status):
    users=User.query.filter_by(approved=status).all()
    return [user.to_dict() for user in users]

@cache.memoize()
def get_category_approval():
    categories=ApproveCategory.query.all()
    return [category.to_dict() for category in categories]

@cache.memoize()
def get_category_approval_by_id(approval_id):
    category=ApproveCategory.query.filter_by(id=approval_id).first()
    return category
            
@cache.memoize()
def get_category_by_id(id):
    category=Category.query.filter_by(cid=id).first()
    return category

@cache.memoize()
def get_product_by_id(id):
    product=Product.query.filter_by(pid=id).first()
    return product