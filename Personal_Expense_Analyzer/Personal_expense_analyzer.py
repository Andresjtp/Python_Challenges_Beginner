

class Expense:

    def __init__(self, category, amount, note):
        self.category = category
        self.amount = amount
        self.note = note

    def info(self):
        print(f"{self.category} - amount: {self.amount} - note: {self.note}")


    class ExpenseTracker:

        def __init__(self):
            self.expenses = []

        def add_expense(self, expense):
            self.expenses.append(expense)
        
        def show_expenses(self):
            for expense in self.expenses:
                expense.info()
        
        def total_spent(self):
            total = 0
            for expense in self.expenses:
                total += expense.amount
            print(f"total spent: {total}")
            return total
        
        def highest_expense(self):
            if not self.expenses:
                return None
            highest = self.expenses[0]
            for expense in self.expenses:
                if expense.amount > highest.amount:
                    highest = expense
            print(f"Highest expense: {highest.category} - {highest.amount}")
            return highest
        
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
            
            




