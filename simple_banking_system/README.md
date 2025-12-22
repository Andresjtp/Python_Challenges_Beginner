# 🏦 Simple Banking System (Advanced Beginner)

## Challenge Overview

This challenge focuses on building a banking system using Python's object-oriented programming principles, conditionals for validation, and functions for managing account operations.

**Core Skills Practiced:**
- Object-Oriented Programming (OOP)
- Conditionals
- Functions
- Data validation

---

## Structure

### Class: `BankAccount`
Represents an individual bank account with three attributes:
- `account_number` - Randomly generated 6-digit account number
- `owner` - Account holder's name
- `balance` - Current account balance

### Class: `Bank`
Manages multiple bank accounts using a list:
- `accounts` - List containing all `BankAccount` objects

---

## Features Implementation

### 1. **Create Account**
```python
def create_account(self, account):
    self.accounts.append(account)
```
**How it works:**
- Accepts a `BankAccount` object as a parameter
- Adds the entire account object to the bank's list of accounts
- Each account gets a unique random account number generated in the `BankAccount` constructor

**Example:**
```python
bank = Bank()
account1 = BankAccount("John Doe", 1000)
bank.create_account(account1)
```

---

### 2. **Deposit Money**
```python
def deposit(self, account_name, amount):
    for account in self.accounts:
        if account_name.lower() == account.owner.lower():
            account.balance += amount
            print(f"Deposited ${amount}. New balance: ${account.balance}")
            return
    print('No account with this name found')
```
**How it works:**
- Iterates through all bank accounts
- Performs case-insensitive name matching using `.lower()`
- Adds the deposit amount to the account's balance
- Returns immediately after successful deposit to prevent processing remaining accounts
- If no matching account is found, displays an error message

**Key concepts:**
- Direct object modification: `account.balance += amount`
- Early return pattern to exit the loop once the account is found
- User-friendly feedback with updated balance

---

### 3. **Withdraw Money with Overdraft Prevention**
```python
def withdraw(self, account_name, amount):
    for account in self.accounts:
        if account_name.lower() == account.owner.lower():
            if amount > account.balance:
                print("Insufficient funds available")
                return
            account.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${account.balance}")
            return
    print("No account with this name found")
```
**How it works:**
- Searches for the account by owner name (case-insensitive)
- **Overdraft prevention**: Checks if withdrawal amount exceeds balance
- If insufficient funds, displays error and exits without processing
- If funds are sufficient, subtracts amount from balance
- Returns after processing to avoid checking remaining accounts

**Key concepts:**
- **Conditional validation**: Prevents negative balances
- **Guard clauses**: Early returns prevent invalid operations
- **Business logic**: Implements real-world banking rules

---

### 4. **Display Account Information**
```python
def account_info(self):
    for account in self.accounts:
        print(f"Account name: {account.owner}\nAccount Balance: {account.balance}\nAccount Number: {account.account_number}")
```
**How it works:**
- Iterates through all accounts in the bank
- Accesses each account's attributes through the object
- Displays formatted information for each account
- Uses `\n` for multi-line output formatting

---

## Key Concepts Demonstrated

### 1. **Object-Oriented Design**
- **Encapsulation**: Account data (owner, balance, account_number) is bundled in the `BankAccount` class
- **Composition**: The `Bank` class contains multiple `BankAccount` objects
- **Single Responsibility**: Each class has a clear purpose

### 2. **Random Account Number Generation**
```python
self.account_number = random.randint(100000, 999999)
```
- Generates a unique 6-digit number for each account
- Simulates real-world banking systems

### 3. **Validation and Error Handling**
- **Overdraft prevention**: Checks balance before withdrawal
- **Account existence validation**: Verifies account exists before operations
- **User feedback**: Clear messages for success and error cases

### 4. **Search Functionality**
- Case-insensitive search allows flexible name matching
- Early return optimization stops searching once account is found

### 5. **List vs Dictionary Choice**
In this implementation, accounts are stored in a **list** rather than a dictionary:
- **Advantage**: Simple to implement, easy to iterate through all accounts
- **Trade-off**: Requires linear search to find accounts by name
- **Alternative approach**: Could use a dictionary with account_number or owner as key for O(1) lookup

---

## Usage Example

```python
# Create a bank
bank = Bank()

# Create accounts
john_account = BankAccount("John Doe", 1000)
jane_account = BankAccount("Jane Smith", 500)

# Add accounts to bank
bank.create_account(john_account)
bank.create_account(jane_account)

# Deposit money
bank.deposit("John Doe", 250)  # New balance: $1250

# Withdraw money
bank.withdraw("Jane Smith", 100)  # New balance: $400

# Attempt overdraft (prevented)
bank.withdraw("Jane Smith", 1000)  # "Insufficient funds available"

# Display all accounts
bank.account_info()
# Output:
# Account name: John Doe
# Account Balance: 1250
# Account Number: 485732
# 
# Account name: Jane Smith
# Account Balance: 400
# Account Number: 927461
```

---

## Potential Enhancements

- Add transfer functionality between accounts
- Implement interest calculation
- Add transaction history
- Use account number instead of name for lookups
- Add PIN/password security
- Support for multiple account types (checking, savings)
- Calculate and display transaction fees
