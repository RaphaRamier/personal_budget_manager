from budget_manager import Expense, Budget


def main():
    print("Welcome to Budget Manager!")
    monthly_income=float(input("Enter your monthly income: "))
    budget=Budget(monthly_income)

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Budget Summary")
        print("3. Exit")
        choice=input("Enter your choice (1/2/3): ")

        if choice == "1":
            name=input("Enter expense name: ")
            amount=float(input("Enter expense amount: "))
            category=input("Enter expense category: ")
            recurring=input("Is this expense recurring? (yes/no): ").lower() == "yes"
            expense=Expense(name, amount, category, recurring)
            budget.add_expenses(expense)
            print("Expense added successfully!")
        elif choice == "2":
            print("\nBudget Summary:")
            print(budget)
        elif choice == "3":
            print("Exiting Budget Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()