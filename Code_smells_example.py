#Code Smells Example for long method
def calculate_total_price(items):
    return sum(calculate_item_price(item) for item in items if item.quantity > 0)

def calculate_item_price(item):
    price = item.price
    return price * 0.9 if price > 100 else price * 0.95
