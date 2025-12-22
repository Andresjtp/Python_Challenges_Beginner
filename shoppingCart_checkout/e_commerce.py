class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.cart = {}  
        self.discount_code = "ATP23"
    
    def add_product(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity
    
    def remove_product(self, product):
        if product in self.cart:
            del self.cart[product]
            print(f"Removed {product.name}")
        else:
            print("Product not in cart")
    
    def update_quantity(self, product, new_quantity):
        if product in self.cart:
            self.cart[product] = new_quantity
        else:
            print("Product not in cart")
    
    def calculate_total(self):
        total = 0
        for product, quantity in self.cart.items():
            total += product.price * quantity
        return total
    
    def apply_discount(self, code):
        total = self.calculate_total()
        if code == self.discount_code:
            total = total * 0.50  
            print(f"Discount applied! Total: ${total:.2f}")
        else:
            print(f"Total: ${total:.2f}")
        return total