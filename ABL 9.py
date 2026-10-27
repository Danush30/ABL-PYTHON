def campus_transport_allocation():
    bus_capacity = 40

    routes = [
        ("Route A", 95),
        ("Route B", 70),
        ("Route C", 125),
        ("Route D", 25)
    ]

    total_buses = 0
    total_unserved = 0

    for route, passengers in routes:
        buses_needed = (passengers + bus_capacity - 1) // bus_capacity
        served_capacity = buses_needed * bus_capacity
        unserved = max(0, passengers - served_capacity)

        total_buses += buses_needed
        total_unserved += unserved

        print(f"\n{route}")
        print("Passenger demand:", passengers)
        print("Buses required:", buses_needed)
        print("Total seating capacity:", served_capacity)
        print("Unserved passengers:", unserved)

    print("\nTotal buses required:", total_buses)
    print("Total unserved passengers:", total_unserved)


if __name__ == "__main__":
    campus_transport_allocation()