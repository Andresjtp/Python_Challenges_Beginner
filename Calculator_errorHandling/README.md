# Calculator with Error Handling

## Challenge Overview

Build a simple calculator that:

- ✅ Takes two numbers and an operation (`+`, `-`, `*`, `/`)
- ✅ Handles invalid operations
- ✅ Handles division by zero
- ✅ Handles invalid number input

**Focus:** Multiple `except` blocks

---

## Solution Explanation

### 1. Calculator Class Structure

The solution uses a `Calculator` class with static methods for each operation:

```python
class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    
    @staticmethod
    def subtract(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2
    
    @staticmethod
    def divide(num1, num2):
        return num1 / num2
```

**Why static methods?** These operations don't need instance-specific data, making them perfect candidates for static methods that can be called directly on the class.

---

### 2. Error Handling Implementation

The main program loop uses **multiple except blocks** to handle different error scenarios:

#### **ValueError Exception**
- Catches invalid number inputs (non-numeric values)
- Catches invalid operations (anything other than `+`, `-`, `*`, `/`)
- Catches empty input fields

```python
except ValueError as ve:
    print(f"Invalid input: {ve}")
```

#### **ZeroDivisionError Exception**
- Specifically handles division by zero cases
- Prevents the program from crashing with a clear error message

```python
except ZeroDivisionError as zde:
    print(f"Invalid input: {zde}")
```

---

### 3. Input Validation

The code validates user input at multiple stages:

1. **Empty Input Check:**
   ```python
   if not first_input:
       raise ValueError("Please enter a number.")
   ```

2. **Number Conversion:**
   ```python
   first_input = int(first_input)
   ```
   - Automatically raises `ValueError` if input cannot be converted to integer

3. **Zero Division Prevention:**
   ```python
   if second_input == 0:
       raise ZeroDivisionError("You can't divide by zero")
   ```

4. **Valid Operation Check:**
   ```python
   if operator not in ['+', '-', '*', '/']:
       raise ValueError("Please enter either +, -, *, or /")
   ```

---

### 4. Program Flow

1. User enters first number → validated and converted to int
2. User enters second number → validated and converted to int
3. User enters operation → validated against allowed operations
4. Appropriate Calculator method is called based on operation
5. Result is displayed
6. If any error occurs, appropriate exception is caught and user-friendly message is shown
7. Loop continues until successful calculation

---

## Key Features

✨ **Separation of Concerns:** Calculator logic is separated from user interaction

✨ **Specific Error Handling:** Different exception types handled separately for clear error messages

✨ **User-Friendly:** Descriptive error messages guide the user to correct input

✨ **Loop Until Success:** Program continues until a valid calculation is performed

---

## Example Usage

### Successful Calculation:
```
Enter a number: 10
Enter a number: 5
enter operator: +
10 + 5 = 15
```

### Invalid Number Input:
```
Enter a number: abc
Invalid input: invalid literal for int() with base 10: 'abc'
```

### Division by Zero:
```
Enter a number: 10
Enter a number: 0
Invalid input: You can't divide by zero
```

### Invalid Operation:
```
Enter a number: 10
Enter a number: 5
enter operator: %
Invalid input: Please enter either +, -, *, or /
```
