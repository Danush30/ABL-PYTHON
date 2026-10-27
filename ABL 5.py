def transaction_audit():
    transactions = [
        ("T101", 500, "CREDIT"),
        ("T102", 200, "DEBIT"),
        ("T103", -100, "CREDIT"),
        ("T102", 300, "DEBIT"),
        ("T104", 15000, "DEBIT"),
        ("T105", 700, "CREDIT"),
        ("T106", 50, "INVALID")
    ]

    seen_ids = set()
    previous_type = None

    for transaction in transactions:
        transaction_id, amount, transaction_type = transaction
        errors = []

        if transaction_id in seen_ids:
            errors.append("Duplicate transaction ID")
        seen_ids.add(transaction_id)

        if amount <= 0:
            errors.append("Invalid amount")

        if transaction_type not in ("CREDIT", "DEBIT"):
            errors.append("Invalid transaction type")

        if amount > 10000:
            errors.append("Suspiciously large transaction")

        if previous_type == "DEBIT" and transaction_type == "DEBIT":
            errors.append("Consecutive debit transactions")

        if transaction_type in ("CREDIT", "DEBIT"):
            previous_type = transaction_type

        print(f"\nTransaction: {transaction}")
        print("Status:", "FLAGGED" if errors else "VALID")
        print("Issues:", ", ".join(errors) if errors else "None")


if __name__ == "__main__":
    transaction_audit()