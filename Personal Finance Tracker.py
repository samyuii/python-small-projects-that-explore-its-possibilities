import pandas as pd
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])

    def add_transaction(self, date, description, amount, category):
        self.transactions = self.transactions.append({"Date": date, "Description": description, "Amount": amount, "Category": category}, ignore_index=True)

    def visualize_data(self):
        category_spending = self.transactions.groupby("Category")["Amount"].sum()
        category_spending.plot(kind="bar")
        plt.xlabel("Categories")
        plt.ylabel("Spending")
        plt.title("Expense Categories")
        plt.show()

if __name__ == "__main__":
    tracker = FinanceTracker()
    tracker.add_transaction("2023-08-01", "Groceries", 150, "Food")
    tracker.add_transaction("2023-08-02", "Internet Bill", 50, "Bills")
    tracker.add_transaction("2023-08-03", "Restaurant", 30, "Food")
    tracker.visualize_data()
