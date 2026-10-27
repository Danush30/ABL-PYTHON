def student_group_formation():
    students = [
        ("Asha", 90), ("Ravi", 75), ("Meena", 85),
        ("Arun", 60), ("Priya", 95), ("Kiran", 70),
        ("Neha", 80), ("Rahul", 65)
    ]

    group_size = 4

    # Sort students by score, highest first.
    students.sort(key=lambda student: student[1], reverse=True)

    groups = [[], []]
    totals = [0, 0]

    # Greedily assign each student to the group with the lower total.
    for student in students:
        index = totals.index(min(totals))
        groups[index].append(student)
        totals[index] += student[1]

    for i, group in enumerate(groups):
        print(f"\nGroup {i + 1}:")
        for name, score in group:
            print(f"{name}: {score}")

        print("Group total:", totals[i])
        print(f"Group average: {totals[i] / len(group):.2f}")

    print("\nDifference between group totals:", abs(totals[0] - totals[1]))


if __name__ == "__main__":
    student_group_formation()