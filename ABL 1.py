def bus_passenger_occupancy():
    capacity = 50
    passengers = 0

    stops = [
        ("Stop 1", 20, 0),
        ("Stop 2", 15, 5),
        ("Stop 3", 10, 8),
        ("Stop 4", 12, 4),
        ("Stop 5", 5, 10)
    ]

    for stop, boarding, alighting in stops:
        passengers -= alighting
        passengers += boarding

        print(f"\n{stop}")
        print("Boarding:", boarding)
        print("Alighting:", alighting)
        print("Passengers:", passengers)

        if passengers > capacity:
            print("Capacity violation!")
        elif passengers < 0:
            print("Invalid passenger count!")
        else:
            print("Within capacity")


if __name__ == "__main__":
    bus_passenger_occupancy()