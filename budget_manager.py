import collections


class Expense:
    def __init__(self, name, amount, category, recurring=False):
        self.name=name
        self.amount=amount
        self.category=category
        self.recurring=recurring

    def __repr__(self):
        return (f"Expense(name='{self.name}',"
                f" amount={self.amount}, "
                f"category='{self.category}', "
                f"recurring={self.recurring})")

    def __str__(self):
        return f"{self.name}: ${self.amount} ({'Recurring' if self.recurring else 'One-time'})"


class Budget:
    def __init__(self, income):
        self.expenses=[]
        self.income=income

    def add_expenses(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def recurring_expenses(self):
        return sum(expense.amount for expense in self.expenses if expense.recurring)

    def monthly_expenses(self):
        return sum(expense.amount for expense in self.expenses if not expense.recurring)

    def forecast_expenses(self):
        categories=collections.defaultdict(list)
        for expense in self.expenses:
            categories[expense.category].append(expense.amount)
        forecasts={category: sum(amounts) / len(amounts) for category, amounts in categories.items()}
        return forecasts

    def savings_analysis(self):
        total_expenses=self.total_expenses()
        savings=self.income - total_expenses
        tips = []

        if savings < 0:
            tips.append("Reduce your spendings.")
        elif savings < 100:
            tips.append('Consider cutting unnecessary expenses.')
        else:
            tips.append("Keep your great job!")

        return savings, tips

    def __repr__(self):
        return f"Budget(monthly_income={self.income}, expenses={self.expenses})"

    def __str__(self):
        expense_list="\n".join(str(expense) for expense in self.expenses)
        total_expenses=self.total_expenses()
        recurring_expenses=self.recurring_expenses()
        monthly_expenses=self.monthly_expenses()
        savings, tips= self.savings_analysis()
        tips_str="\n".join(tips)
        return (f"Budget for the month:\n"
                f"Monthly Income: ${self.income}\n"
                f"Total Expenses: ${total_expenses}\n"
                f"Recurring Expenses: ${recurring_expenses}\n"
                f"Monthly One-time Expenses: ${monthly_expenses}\n"
                f"Savings: ${savings}\n"
                f"Tips: {tips_str}\n"
                f"Expenses:\n{expense_list}")
