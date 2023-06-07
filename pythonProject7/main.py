#This is an expense tracker
import matplotlib.pyplot as plt


def budget_tracker():
    income = float(input("Enter your income for the month: "))
    expenses = []
    total_expenses = 0

    while True:
        expense = input("Enter an expense (or 'q' to finish): ")
        if expense.lower() == 'q':
            break
        expense_amount = float(input("Enter the expense amount: "))
        expenses.append((expense, expense_amount))
        total_expenses += expense_amount

    remaining_balance = income - total_expenses

    # Generate a pie chart of expenses
    expense_labels = [expense[0] for expense in expenses]
    expense_amounts = [expense[1] for expense in expenses]

    plt.figure(figsize=(8, 6))
    plt.pie(expense_amounts, labels=expense_labels, autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.show()

    print("\n\n********** Monthly Budget Summary **********")
    print("Income:", income)
    print("Total Expenses:", total_expenses)
    print("Remaining Balance:", remaining_balance)


# Run the budget tracker
budget_tracker()

