# 🛒 Shopping Cart + Checkout System

## Challenge Overview

This challenge focuses on building an e-commerce shopping cart system using Python's lists, dictionaries, and object-oriented programming to manage products and calculate totals with discount functionality.

**Core Skills Practiced:**
- Lists
- Dictionaries
- Object-Oriented Programming (OOP)
- Mathematical calculations
- Conditional logic

---

## Structure

### Class: `Product`
Represents an individual product with two attributes:
- `name` - Product name
- `price` - Product price

### Class: `Cart`
Manages a shopping cart using a dictionary:
- `cart` - Dictionary where keys are Product objects and values are quantities
- `total_price` - Running total of cart value
- `discount_code` - Valid discount code for promotions

---

## Features Implementation

### 1. **Add Product to Cart**
```python
def add_product(self, product, quantity):
    self.cart[product] = quantity
```
**How it works:**
- Accepts a `Product` object and quantity as parameters
- Stores the Product as the key and quantity as the value in the dictionary
- This structure allows tracking multiple different products and their quantities

**Example:**
```python
cart = Cart()
laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 29.99)

cart.add_product(laptop, 1)
cart.add_product(mouse, 2)
# cart = {laptop: 1, mouse: 2}
```

---

### 2. **Remove Product from Cart**
```python
def remove_product(self, product):
    self.cart.pop(product)
```
**How it works:**
- Uses `.pop()` to remove a product from the cart dictionary
- Takes the Product object as the key to identify which product to remove
- Completely removes the product regardless of quantity

**Key concept:**
- Using the Product object itself as the dictionary key allows direct product removal

---

### 3. **Update Quantity**
```python
def update_quantity(self, amount):
    for products in self.cart:
        self.cart[products] += amount

def reduce_quantity(self, amount):
    for products in self.cart:
        self.cart[products] -= amount
```
**How it works:**
- `update_quantity`: Iterates through all products and increases their quantities
- `reduce_quantity`: Iterates through all products and decreases their quantities
- Both methods modify the quantity values in the dictionary

**Current implementation:**
- Updates ALL products in the cart by the same amount
- To update a specific product, you would pass the product as a parameter:
  ```python
  def update_quantity(self, product, new_quantity):
      if product in self.cart:
          self.cart[product] = new_quantity
  ```

---

### 4. **Calculate Total**
```python
def total(self):
    for products in self.cart:
        self.total_price += products.price * self.cart[products]
    return
    print(f"total price: ${self.total_price}")
```
**How it works:**
- Iterates through each Product object in the cart
- Multiplies the product's price by its quantity
- Accumulates the total in `self.total_price`
- Uses the Product object's `.price` attribute to access pricing

**Formula:** `Total = Σ(price × quantity)` for all products

**Note:** The `print` statement after `return` won't execute. To fix:
```python
def total(self):
    for products in self.cart:
        self.total_price += products.price * self.cart[products]
    print(f"total price: ${self.total_price}")
    return self.total_price
```

---

### 5. **Apply Simple Discount Rule**
```python
def discount_rule(self, discnum):
    if discnum == self.discount_code:
        self.total_price = self.total_price * .50
```
**How it works:**
- Accepts a discount code string as input
- Compares it with the stored valid discount code ("ATP23")
- If codes match, applies a 50% discount to the total price
- Uses conditional logic to validate before applying discount

**Discount calculation:** `discounted_price = total_price × 0.50`

**Example:**
```python
cart.total()  # Calculates total
cart.discount_rule("ATP23")  # Applies 50% off
```

---

## Key Concepts Demonstrated

### 1. **Dictionary with Objects as Keys**
```python
self.cart[product] = quantity
# {Product("Laptop", 999.99): 1, Product("Mouse", 29.99): 2}
```
- Uses Product objects as dictionary keys
- Values represent quantities
- Allows storing complex data structures

### 2. **Object Attribute Access**
```python
products.price  # Access the price attribute of Product object
```
- When iterating through the dictionary, the key is a Product object
- Can access any attribute (`.name`, `.price`) of the Product

### 3. **Mathematical Operations**
- **Multiplication:** `price × quantity` for subtotals
- **Addition:** Accumulating total with `+=`
- **Percentage discount:** `total × 0.50` for 50% off

### 4. **Dictionary Iteration**
```python
for products in self.cart:
    # products = Product object (the key)
    # self.cart[products] = quantity (the value)
```
- Iterating over a dictionary gives you the keys
- Access values using `dictionary[key]`

---

## Usage Example

```python
# Create products
laptop = Product("Laptop", 999.99)
mouse = Product("Wireless Mouse", 29.99)
keyboard = Product("Mechanical Keyboard", 89.99)

# Create cart
cart = Cart()

# Add products to cart
cart.add_product(laptop, 1)     # 1 laptop
cart.add_product(mouse, 2)      # 2 mice
cart.add_product(keyboard, 1)   # 1 keyboard

# Calculate total
cart.total()
# Total: $1149.96 (999.99 + 29.99*2 + 89.99)

# Apply discount code
cart.discount_rule("ATP23")
# New total: $574.98 (50% off)

# Update quantities
cart.update_quantity(1)  # Adds 1 to all product quantities

# Remove a product
cart.remove_product(mouse)  # Removes mouse completely
```

---

## Data Structure Visualization

```python
# Cart dictionary structure:
{
    Product("Laptop", 999.99): 1,
    Product("Mouse", 29.99): 2,
    Product("Keyboard", 89.99): 1
}

# Key: Product object with name and price
# Value: Integer quantity
```

---

## Potential Enhancements

- Add inventory management (stock levels)
- Implement multiple discount codes with different percentages
- Add tax calculation
- Create a checkout summary display
- Add shipping costs based on total or weight
- Implement quantity validation (prevent negative quantities)
- Add "update specific product" instead of updating all
- Create a view/display cart contents method
- Add product categories or tags
- Implement a search/filter products feature
- Save cart state to file for persistence
- Calculate subtotals for individual products
