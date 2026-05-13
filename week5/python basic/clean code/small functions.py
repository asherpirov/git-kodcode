def is_valid_email(user_email):
    if not user_email:
        print("Invalid user")
        return False
    return True

def is_valid_quantity(quantity, stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return False
    return True

def calculate_base_price(product_price, quantity):
    return product_price * quantity

def apply_discount(price, quantity):
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def update_stock(stock, quantity):
    return stock - quantity

def process_order_details(user_email, product_name,quantity, final_price):
    order_status = "confirmed"
    print(f"Order {order_status}: {user_email} bought {quantity}x {product_name} for ${final_price}")
    return user_email, product_name, quantity, final_price, order_status

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not is_valid_email(user_email):
        return None
    if not is_valid_quantity(quantity, stock):
        return None

    base_price = calculate_base_price(product_price, quantity)
    final_price = apply_discount(base_price, quantity)
    stock = update_stock(stock, quantity)
    return process_order_details(user_email, product_name, quantity, final_price)
