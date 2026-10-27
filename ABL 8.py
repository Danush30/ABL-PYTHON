def library_fine_reconciliation():
    fine_per_day = 5
    borrowing_records = [
        ("B101", 14, 2),
        ("B102", 7, 0),
        ("B103", 14, 5),
        ("B104", 10, 3),
        ("B105", 7, 1)
    ]

    available_books = 10
    total_fines = 0

    for book_id, borrowed_days, delay_days in borrowing_records:
        fine = delay_days * fine_per_day
        total_fines += fine

        print(f"\nBook ID: {book_id}")
        print("Borrowed days:", borrowed_days)
        print("Delay days:", delay_days)
        print("Fine: ₹", fine)

        if delay_days > 0:
            print("Status: OVERDUE")
        else:
            print("Status: RETURNED ON TIME")

        available_books += 1

    print("\nTotal fines collected: ₹", total_fines)
    print("Available books after returns:", available_books)


if __name__ == "__main__":
    library_fine_reconciliation()
    