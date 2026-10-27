def branch_expense_analysis():
    branches = ["Branch A", "Branch B", "Branch C"]
    categories = ["Rent", "Salaries", "Utilities", "Transport"]

    expenses = [
        [20000, 50000, 8000, 5000],
        [25000, 45000, 10000, 7000],
        [18000, 55000, 9000, 6000]
    ]

    category_totals = [0] * len(categories)
    grand_total = 0

    for i, branch in enumerate(branches):
        total = sum(expenses[i])
        average = total / len(categories)
        grand_total += total

        print(f"\n{branch}")
        for j, category in enumerate(categories):
            print(f"{category}: ₹{expenses[i][j]}")
            category_totals[j] += expenses[i][j]

        print("Total expenses: ₹", total)
        print(f"Average expense: ₹{average:.2f}")

    print("\nCategory-wise totals:")
    for i, category in enumerate(categories):
        print(f"{category}: ₹{category_totals[i]}")

    largest_category = categories[category_totals.index(max(category_totals))]
    print("\nLargest expense category:", largest_category)
    print("Grand total expenses: ₹", grand_total)


if __name__ == "__main__":
    branch_expense_analysis()