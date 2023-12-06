import matplotlib.pyplot as plt

class Flight:
    def __init__(self, number, distance, price, duration, layovers):
        self.number = number
        self.distance = distance
        self.price = price
        self.duration = duration
        self.layovers = layovers

def efficient_flight(flights):
    total_distance = 0
    total_price = 0

    for flight in flights:
        if total_distance + flight.distance <= 1000:
            total_distance += flight.distance
            total_price += flight.price

    return flights[-1]

def visualize_data(flights):
    ratios = [flight.price / flight.distance for flight in flights]
    flight_numbers = [flight.number for flight in flights]

    plt.figure(figsize=(8, 6))
    plt.bar(flight_numbers, ratios, color='skyblue')
    plt.xlabel('Flight Number')
    plt.ylabel('Cost-Distance Ratio')
    plt.title('Flight Cost-to-Distance Ratio Visualization')
    plt.savefig('static/flight_visualization.png')

def bubble_sort(flights):
    n = len(flights)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            ratio_j = flights[j].price / flights[j].distance
            ratio_j1 = flights[j + 1].price / flights[j + 1].distance

            if ratio_j > ratio_j1:
                flights[j], flights[j + 1] = flights[j + 1], flights[j]

def main():
    # Test cases
    test_flights = [
        Flight("F1", 500, 150, 2, 1),
        Flight("F2", 800, 200, 3, 0),
        Flight("F3", 600, 180, 2.5, 2),
        Flight("F4", 700, 160, 2.3, 1)
    ]

    # Visualize the test data
    visualize_data(test_flights)

    # User input for flights
    flights = []
    num_flights = int(input("Enter the number of flights: "))

    for i in range(num_flights):
        number = input(f"Enter Flight {i + 1} Number: ")
        distance = int(input(f"Enter Distance for Flight {i + 1} (in km): "))
        price = float(input(f"Enter Ticket Price for Flight {i + 1} (in $): "))
        duration = float(input(f"Enter Duration for Flight {i + 1} (in hours): "))
        layovers = int(input(f"Enter Number of Layovers for Flight {i + 1}: "))

        flights.append(Flight(number, distance, price, duration, layovers))

    # Bubble sort flights based on the lowest cost-to-distance ratio
    bubble_sort(flights)

    # Display the sorted data
    sorted_data = []
    for flight in flights:
        sorted_data.append(f"Flight {flight.number}: {flight.price / flight.distance:.4f}")

    # Greedy selection
    selected_flight = efficient_flight(flights)

    # Display the result
    selected_flight_info = (
        f"Flight Number: {selected_flight.number}\n"
        f"Distance: {selected_flight.distance} km\n"
        f"Ticket Price: ${selected_flight.price}\n"
        f"Duration: {selected_flight.duration} hours\n"
        f"Layovers: {selected_flight.layovers}"
    )

    return sorted_data, selected_flight_info

