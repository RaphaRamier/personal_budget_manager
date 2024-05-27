import pytest
from budget_manager import Expense, Budget


def test_add_expense():
    budget=Budget(2500)
    expense=Expense("Rent", 1200, "Housing", recurring=True)
    budget.add_expenses(expense)
    assert len(budget.expenses) == 1


def test_total_expenses():
    budget=Budget(2500)
    expense1=Expense("Rent", 1200, "Housing", recurring=True)
    expense2=Expense("Groceries", 300, "Food")
    budget.add_expenses(expense1)
    budget.add_expenses(expense2)
    assert budget.total_expenses() == 1500


def test_recurring_expenses():
    budget=Budget(2500)
    expense1=Expense("Rent", 1200, "Housing", recurring=True)
    expense2=Expense("Internet", 100, "Utilities", recurring=True)
    expense3=Expense("Groceries", 300, "Food")
    budget.add_expenses(expense1)
    budget.add_expenses(expense2)
    budget.add_expenses(expense3)
    assert budget.recurring_expenses() == 1300


def test_monthly_expenses():
    budget=Budget(2500)
    expense1=Expense("Rent", 1200, "Housing", recurring=True)
    expense2=Expense("Groceries", 300, "Food")
    expense3=Expense("Internet", 100, "Utilities", recurring=True)
    budget.add_expenses(expense1)
    budget.add_expenses(expense2)
    budget.add_expenses(expense3)
    assert budget.monthly_expenses() == 300


def test_forecast_expenses():
    budget=Budget(2500)
    expense1=Expense("Groceries", 300, "Food")
    expense2=Expense("Groceries", 400, "Food")
    expense3=Expense("Entertainment", 200, "Leisure")
    budget.add_expenses(expense1)
    budget.add_expenses(expense2)
    budget.add_expenses(expense3)
    forecasts=budget.forecast_expenses()
    assert forecasts["Food"] == 350
    assert forecasts["Leisure"] == 200


def test_savings_analysis():
    budget=Budget(2500)
    expense1=Expense("Rent", 1200, "Housing", recurring=True)
    expense2=Expense("Electricity Bill", 150, "Utilities", recurring=True)
    expense3=Expense("Groceries", 300, "Food")
    expense4=Expense("Internet", 100, "Utilities", recurring=True)
    expense5=Expense("Entertainment", 200, "Leisure")
    budget.add_expenses(expense1)
    budget.add_expenses(expense2)
    budget.add_expenses(expense3)
    budget.add_expenses(expense4)
    budget.add_expenses(expense5)
    savings, tips=budget.savings_analysis()
    assert savings == 550
    assert "Keep your great job!" in tips[0]


if __name__ == "__main__":
    pytest.main()
