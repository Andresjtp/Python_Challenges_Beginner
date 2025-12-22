# Personal Expense Analyzer

## Challenge Description

This beginner-level Python challenge focuses on building a **Personal Expense Analyzer** to practice core programming skills including **lists, dictionaries, OOP (Object-Oriented Programming), and loops**.

### Challenge Requirements

The program must implement two classes with the following structure:

#### Class: `Expense`
- `category` - The category of the expense (e.g., Food, Transport, Entertainment)
- `amount` - The monetary amount spent
- `note` - Additional notes or description about the expense

#### Class: `ExpenseTracker`
- Stores a list of expenses
- Provides the following features:
  1. **Add expense** - Add new expenses to the tracker
  2. **Show all expenses** - Display all recorded expenses
  3. **Total spent** - Calculate and display the total amount spent across all expenses
  4. **Total per category** - Calculate spending totals grouped by category
  5. **Find highest expense** - Identify and display the single most expensive item

---

## Code Implementation Explanation

### 1. The `Expense` Class

```python
class Expense:
    def __init__(self, category, amount, note):
        self.category = category
        self.amount = amount
        self.note = note
```

The `Expense` class represents a single expense transaction with three attributes:
- **category**: Type of expense
- **amount**: How much was spent
- **note**: Additional details

**The `info()` method:**
```python
def info(self):
    print(f"{self.category} - amount: {self.amount} - note: {self.note}")
```
This method displays the expense details in a formatted string using f-strings.

---

### 2. The `ExpenseTracker` Class

```python
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
```

The `ExpenseTracker` class manages multiple expenses using a list called `self.expenses`. This is the core data structure that stores all `Expense` objects.

#### Method: `add_expense()`
```python
def add_expense(self, expense):
    self.expenses.append(expense)
```
Adds a new `Expense` object to the expenses list. Uses the `append()` method to add items to the list.

#### Method: `show_expenses()`
```python
def show_expenses(self):
    for expense in self.expenses:
        expense.info()
```
**Demonstrates loops**: Iterates through each expense in the list using a `for` loop and calls the `info()` method on each expense object to display its details.

#### Method: `total_spent()`
```python
def total_spent(self):
    total = 0
    for expense in self.expenses:
        total += expense.amount
    print(f"total spent: {total}")
    return total
```
**Demonstrates loops and accumulation**:
- Initializes a `total` variable at 0
- Loops through all expenses
- Accumulates the sum by adding each expense's amount
- Prints and returns the total

#### Method: `highest_expense()`
```python
def highest_expense(self):
    if not self.expenses:
        return None
    highest = self.expenses[0]
    for expense in self.expenses:
        if expense.amount > highest.amount:
            highest = expense
    print(f"Highest expense: {highest.category} - {highest.amount}")
    return highest
```
**Demonstrates conditional logic and loops**:
- First checks if the list is empty (edge case handling)
- Assumes the first expense is the highest
- Loops through all expenses comparing amounts
- Updates `highest` whenever a larger expense is found
- Returns the expense with the maximum amount

#### Method: `total_per_category()`
```python
def total_per_category(self):
    category_totals = {}
    for expense in self.expenses:
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount
    for category, total in category_totals.items():
        print(f"{category}: {total}")
    return category_totals
```
**Demonstrates dictionaries and loops**:
- Creates an empty dictionary `category_totals` to store category sums
- Loops through all expenses
- Uses conditional logic to check if a category already exists in the dictionary
- If it exists, adds to the existing total; if not, creates a new entry
- Loops through the dictionary items to print each category with its total
- Returns the dictionary containing all category totals

---

## Key Programming Concepts Practiced

1. **Object-Oriented Programming (OOP)**
   - Creating classes with `__init__` constructors
   - Defining methods within classes
   - Using `self` to reference instance attributes
   - Creating objects and calling their methods

2. **Lists**
   - Storing multiple objects in a list
   - Appending items to lists
   - Iterating through lists with for loops
   - Accessing list elements by index

3. **Dictionaries**
   - Creating empty dictionaries
   - Adding key-value pairs
   - Checking if keys exist
   - Iterating through dictionary items

4. **Loops**
   - For loops to iterate through collections
   - Accumulating values in loops
   - Finding maximum values through iteration

5. **Conditional Logic**
   - If-else statements for decision making
   - Checking for empty lists
   - Comparing values

---

## Example Usage

```python
# Create an expense tracker
tracker = ExpenseTracker()

# Add some expenses
tracker.add_expense(Expense("Food", 50.00, "Grocery shopping"))
tracker.add_expense(Expense("Transport", 30.00, "Gas"))
tracker.add_expense(Expense("Food", 25.00, "Restaurant"))
tracker.add_expense(Expense("Entertainment", 60.00, "Concert tickets"))

# Display all expenses
tracker.show_expenses()

# Get total spending
tracker.total_spent()

# Find highest expense
tracker.highest_expense()

# Get totals by category
tracker.total_per_category()
```

Expected output:
```
Food - amount: 50.0 - note: Grocery shopping
Transport - amount: 30.0 - note: Gas
Food - amount: 25.0 - note: Restaurant
Entertainment - amount: 60.0 - note: Concert tickets
total spent: 165.0
Highest expense: Entertainment - 60.0
Food: 75.0
Transport: 30.0
Entertainment: 60.0
```
