def food_waste_monitoring():
    days = [
        ("Monday", 200, 180),
        ("Tuesday", 250, 220),
        ("Wednesday", 180, 150),
        ("Thursday", 300, 240),
        ("Friday", 220, 200)
    ]

    waste_limit = 15

    for day, prepared, served in days:
        leftovers = prepared - served
        waste_percentage = leftovers / prepared * 100

        print(f"\nDay: {day}")
        print("Meals prepared:", prepared)
        print("Meals served:", served)
        print("Leftover meals:", leftovers)
        print(f"Wastage: {waste_percentage:.2f}%")

        if waste_percentage > waste_limit:
            print("Warning: Wastage exceeds the limit!")
        else:
            print("Wastage is within the limit.")


if __name__ == "__main__":
    food_waste_monitoring()